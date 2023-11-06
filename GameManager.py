# cada clase, cada archivo
# GameManager, donde se realizan la mayoría de las tareas del juego

import os
import pickle
import random
import time

import ClassesRPG.Archer as Cl_Archer
import ClassesRPG.Bard as Cl_Bard
import ClassesRPG.Necromancer as Cl_Necro
import ClassesRPG.Paladin as Cl_Paladin
import ClassesRPG.Sorcerer as Cl_Sorcerer
import ClassesRPG.Tank as Cl_Tank
import ClassesRPG.Thief as Cl_Thief
import ClassesRPG.Warrior as Cl_Warrior
import ClassesRPG.Wizard as Cl_Wizard
import PointOfInterest as POI
import Enemy
import Constants
import Item


global player_info
global Player


class GameManager:
    def __init__(self):
        pass

    def initializeGame(self):
        global player_info
        global Player
        self.showMessage(Constants.WELCOMING_MESSAGE)
        self.showMessage(Constants.MAIN_MENU_OPTIONS)
        while True:
            player_main_menu_choice = self.getPlayerChoice()
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            if player_main_menu_choice == "1":  # nueva partida
                if os.path.isfile("savefile.pickle"):
                    if not self.confirmPlayerSaveFileDeletion():
                        return self.initializeGame()
                self.createCharacter()
                self.clearScreen()
                self.showMessage(Constants.MAIN_MENU_MESSAGE_GAME_LOADING)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.clearScreen()
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                return self.beginGame()
            elif player_main_menu_choice == "2":  # cargar partida
                self.loadGame()
                return self.idleState()
            elif player_main_menu_choice == "3":  # instrucciones
                self.clearScreen()
                return self.initializeGame()
            elif player_main_menu_choice == "4":  # salir
                return exit(0)
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_MAIN_MENU_OPTION)

    def beginGame(self):
        global player_info
        if self.checkIfPlayerIsInLocation(POI.Muldraugh):
            self.showMessage(Constants.INTRO_MESSAGE_MULDRAUGH)
        elif self.checkIfPlayerIsInLocation(POI.Riverside):
            self.showMessage(Constants.INTRO_MESSAGE_RIVERSIDE)
        self.waitForButtonPress(Constants.PRESS_ENTER_TO_CONTINUE)
        return self.idleState()

    def idleState(self):
        global player_info
        global Player
        Player.mana = Player.max_mana
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        while True:
            self.showMessage(Constants.WORLD_PLAYER_DECIDE_WHAT_TO_DO)
            player_world_decision = self.getPlayerChoice()
            if player_world_decision == "1":  # viajar
                return self.getTravelOptions(player_info["location"])
            elif player_world_decision == "2":  # Inspeccionarse
                self.showStats()
                self.manageInventory()
            elif player_world_decision == "3":  # guardar y salir
                self.saveGame()
                return exit(0)

    def getTravelOptions(self, location_classobj):
        global player_info
        self.showCombinedMessage(Constants.WORLD_PLAYER_IS_IN_POI, player_info["location"].name)
        while True:
            self.showMessage("\n" + Constants.WORLD_AVAILABLE_POI)
            for i in range(len(location_classobj.connected_locations)):
                self.showCombinedMessage(f"{i + 1}.", location_classobj.connected_locations[i].name)
            self.showMessage("\n")
            return self.confirmTravelOption(location_classobj)

    def confirmTravelOption(self, location_classobj):
        while True:
            while True:
                player_travel_choice = self.getPlayerChoice()
                if player_travel_choice.isnumeric():
                    break
                elif player_travel_choice in Constants.PLAYER_PROMPT_TO_RETURN:
                    return self.idleState()
                else:
                    self.showWarning(Constants.WARNING_MESSAGE_CHOICE_IS_NOT_NUMERIC)
            for i in range(len(location_classobj.connected_locations)):
                if player_travel_choice == f"{i + 1}":
                    self.showMessage("\n" + location_classobj.connected_locations[i].description)
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.WORLD_TRAVEL_CONFIRMATION)
                    while True:
                        player_travel_choice_confirmation = self.getPlayerChoice()
                        if player_travel_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_YES:
                            return self.travelingTo(location_classobj.connected_locations[i])
                        elif player_travel_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                            break
                        else:
                            self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)
                    break
            if 0 < (int(player_travel_choice)) < len(location_classobj.connected_locations):
                return self.getTravelOptions(location_classobj)
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_TRAVEL_CHOICE)

    def travelingTo(self, location_classobj):
        global player_info
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showCombinedMessage(Constants.WORLD_TRAVEL_GOING_TO_PLACE, location_classobj.name)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        if location_classobj.classification == "safe":
            player_info["location"] = location_classobj
            self.showCombinedMessage(Constants.WORLD_PLAYER_HAS_ARRIVED_TO, location_classobj.name)
            return self.idleState()
        elif location_classobj.classification == "shop":
            return self.shopping(location_classobj)
        elif location_classobj.classification == "unsafe":
            player_info["location"] = location_classobj
            return self.getBattleChance(location_classobj.classification)
        else:
            player_info["location"] = location_classobj
            self.getItemDropChanceAndGetItem(location_classobj.possible_items)
            return self.getBattleChance(location_classobj.classification)

    def getBattleChance(self, location_classification_str):
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.SOMEONE_APPROACHES)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        if random.random() < (80 / 100):
            return self.generateRandomEnemyAndFight(location_classification_str)
        else:
            self.showMessage(Constants.SOMEONE_APPROACHES_AND_IS_NOT_ENEMY)
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            return self.idleState()

    def generateRandomEnemyAndFight(self, location_classification_str):
        self.showMessage(Constants.SOMEONE_APPROACHES_AND_IS_ENEMY)
        if location_classification_str == "unsafe" or location_classification_str == "searchable common":
            random_name = random.choice(Constants.ENEMY_NAMES)
            random_health = Constants.RANDOM_ENEMY_HEALTH_FOR_COMMON_ITEMS_LOCATION
            random_dmg = Constants.RANDOM_ENEMY_DMG_FOR_COMMON_ITEMS_LOCATION
            RandomEnemy = Enemy.Enemy(random_name, random_health, random_dmg)
            return self.battle(RandomEnemy, "low")
        elif location_classification_str == "searchable uncommon":
            random_name = random.choice(Constants.ENEMY_NAMES)
            random_health = Constants.RANDOM_ENEMY_HEALTH_FOR_UNCOMMON_ITEMS_LOCATION
            random_dmg = Constants.RANDOM_ENEMY_DMG_FOR_UNCOMMON_ITEMS_LOCATION
            RandomEnemy = Enemy.Enemy(random_name, random_health, random_dmg)
            return self.battle(RandomEnemy, "medium")
        elif location_classification_str == "searchable legendary":
            random_name = random.choice(Constants.ENEMY_NAMES)
            random_health = Constants.RANDOM_ENEMY_HEALTH_FOR_LEGENDARY_ITEMS_LOCATION
            random_dmg = Constants.RANDOM_ENEMY_DMG_FOR_LEGENDARY_ITEMS_LOCATION
            RandomEnemy = Enemy.Enemy(random_name, random_health, random_dmg)
            return self.battle(RandomEnemy, "high")

    def getItemDropChanceAndGetItem(self, item_list):
        item_pool = []
        for i in range(len(item_list)):
            if self.calculateChance(50):
                item_pool.append(item_list[i])
        if self.calculateChance(75):
            item_to_be_found = item_pool[random.randint(0, len(item_pool))]
            if item_to_be_found.item_type == "weapon":
                player_info["backpack_items"]["weapons"].append(item_to_be_found)
                self.showCombinedMessage(Constants.WORLD_FORAGE_ITEM_FOUND, item_to_be_found.name)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.saveGame()
                return None
            if item_to_be_found.item_type == "potion":
                player_info["backpack_items"]["potions"].append(item_to_be_found)
                self.showCombinedMessage(Constants.WORLD_FORAGE_ITEM_FOUND, item_to_be_found.name)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.saveGame()
                return None
            if item_to_be_found.item_type == "armor":
                player_info["backpack_items"]["armors"].append(item_to_be_found)
                self.showCombinedMessage(Constants.WORLD_FORAGE_ITEM_FOUND, item_to_be_found.name)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.saveGame()
                return None
        else:
            self.showMessage(Constants.WORLD_FORAGE_NO_ITEM_FOUND)
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            return self.idleState()

    def showStats(self):
        global Player
        self.showMessage("\n"+f"|| {Player.name} ||"+"\n")
        self.showMessage(f"Salud: {Player.health:.2f}\n"
                         f"Defensa: {Player.armor}\n"
                         f"Mana: {Player.mana}\n"
                         f"Fuerza: {Player.str}\n"
                         f"Agilidad: {Player.agi}\n"
                         f"Inteligencia: {Player.int}\n"
                         f"Fe: {Player.faith}\n"
                         f"Puntería: {Player.acc}\n"
                         f"Resistencia mágica: {Player.res_magic}\n"
                         f"Resistencia física: {Player.res_phys}\n"
                         f"Dinero: {Player.money}\n"
                         f"Nivel: {Player.lvl}\n"
                         f"Experiencia: {Player.exp}/100\n")

    def manageInventory(self, shop=False, battle=False):
        global player_info
        self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE)
        counter_for_potions = 0
        counter_for_armors = 0
        # counter 'i' will work as a counter for weapons
        possible_inventory_choices = {}
        self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE_WEAPONS)
        if len(player_info["backpack_items"]["weapons"]) == 0:
            self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE_NO_ITEMS)
        else:
            for i in range(len(player_info["backpack_items"]["weapons"])):
                self.showMessage(f"{i + 1}. {player_info["weapons"][i]}")
                possible_inventory_choices[f"{i + 1}"] = player_info["weapons"][i]
                counter_for_potions = counter_for_potions + (i + 1)
        self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE_POTIONS)
        if len(player_info["backpack_items"]["potions"]) == 0:
            self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE_NO_ITEMS)
        else:
            for i in range(len(player_info["backpack_items"]["potions"])):
                self.showMessage(f"{counter_for_potions + 1}. {player_info["potions"][i]}")
                counter_for_potions = counter_for_potions + 1
                possible_inventory_choices[f"{counter_for_potions}"] = player_info["potions"][i]
                counter_for_armors = counter_for_armors + counter_for_potions
        self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE_ARMORS)
        if len(player_info["backpack_items"]["armors"]) == 0:
            self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE_NO_ITEMS)
        else:
            for i in range(len(player_info["backpack_items"]["armors"])):
                self.showMessage(f"{counter_for_armors + 1}. {player_info["armors"][i]}")
                counter_for_armors = counter_for_armors + 1
                possible_inventory_choices[f"{counter_for_armors}"] = player_info["potions"][i]
        self.showMessage(Constants.PLAYER_INVENTORY_MESSAGE_ACTIONS)
        while True:
            player_inventory_action_choice = self.getPlayerChoice()
            if player_inventory_action_choice in Constants.PLAYER_INVENTORY_ACTION_SET_SELECT:
                if len(possible_inventory_choices) > 0:
                    player_inventory_item_selected = self.getPlayerChoice(Constants.PLAYER_PROMPT_ITEM_NUMBER)
                    self.showMessage(Constants.PLAYER_INVENTORY_SELECTED_ITEM_OPTIONS)
                    while True:
                        player_inventory_selected_item_action_choice = self.getPlayerChoice()
                        if player_inventory_selected_item_action_choice == Constants.PLAYER_INVENTORY_ACTION_SET_DISCARD:  # descarta el item
                            if possible_inventory_choices[player_inventory_item_selected].item_type == "weapon":
                                player_info["backpack_items"]["weapons"].remove(
                                    possible_inventory_choices[player_inventory_item_selected])
                                self.showCombinedMessage(Constants.PLAYER_INVENTORY_ITEM_WAS_DISCARDED, possible_inventory_choices[player_inventory_item_selected].name)
                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                return self.manageInventory()
                            elif possible_inventory_choices[player_inventory_item_selected].item_type == "potion":
                                player_info["backpack_items"]["potions"].remove(
                                    possible_inventory_choices[player_inventory_item_selected])
                                self.showCombinedMessage(Constants.PLAYER_INVENTORY_ITEM_WAS_DISCARDED, possible_inventory_choices[player_inventory_item_selected].name)
                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                return self.manageInventory()
                            elif possible_inventory_choices[player_inventory_item_selected].item_type == "armor":
                                player_info["backpack_items"]["armors"].remove(
                                    possible_inventory_choices[player_inventory_item_selected])
                                self.showCombinedMessage(Constants.PLAYER_INVENTORY_ITEM_WAS_DISCARDED, possible_inventory_choices[player_inventory_item_selected].name)
                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                return self.manageInventory()
                        elif player_inventory_selected_item_action_choice == Constants.PLAYER_INVENTORY_ACTION_SET_EQUIP:  # se equipa el item
                            if possible_inventory_choices[player_inventory_item_selected].item_type == "weapon":
                                if player_info["weapon_1"]:
                                    self.showMessage(Constants.PLAYER_INVENTORY_ALREADY_HAS_WEAPON)
                                    player_inventory_replace_weapon_choice = self.getPlayerChoice()
                                    while True:
                                        if player_inventory_replace_weapon_choice in Constants.PLAYER_PROMPT_SET_FOR_YES:
                                            player_info["backpack_items"]["weapons"].append(player_info["weapon_1"])
                                            weapon_new_equipped = possible_inventory_choices[player_inventory_item_selected]
                                            player_info["backpack_items"]["weapons"].remove(possible_inventory_choices[player_inventory_item_selected])
                                            player_info["weapon_1"] = weapon_new_equipped
                                            self.showMessage(Constants.PLAYER_INVENTORY_NEW_WEAPON_EQUIPPED)
                                            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                            return self.manageInventory()
                                        elif player_inventory_replace_weapon_choice in Constants.PLAYER_PROMPT_SET_FOR_NO:
                                            break
                                        else:
                                            self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)
                                    break
                                elif possible_inventory_choices[player_inventory_item_selected].item_type == "armor":
                                    if player_info["helmet"]:
                                        self.showMessage(Constants.PLAYER_INVENTORY_ALREADY_HAS_ARMOR)
                                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                        player_inventory_replace_armor_choice = self.getPlayerChoice()
                                        while True:
                                            if player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_YES:
                                                player_info["backpack_items"]["armors"].append(player_info["helmet"])
                                                armor_new_equipped = possible_inventory_choices[player_inventory_item_selected]
                                                player_info["backpack_items"]["armors"].remove(
                                                    possible_inventory_choices[player_inventory_item_selected])
                                                player_info["helmet"] = armor_new_equipped
                                                self.showMessage(Constants.PLAYER_INVENTORY_NEW_ARMOR_EQUIPPED)
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                return self.manageInventory()
                                            elif player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_NO:
                                                break
                                            else:
                                                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)
                                        break
                                    elif player_info["breastplate"]:
                                        self.showMessage(Constants.PLAYER_INVENTORY_ALREADY_HAS_ARMOR)
                                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                        player_inventory_replace_armor_choice = self.getPlayerChoice()
                                        while True:
                                            if player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_YES:
                                                player_info["backpack_items"]["armors"].append(player_info["breastplate"])
                                                armor_new_equipped = possible_inventory_choices[player_inventory_item_selected]
                                                player_info["backpack_items"]["armors"].remove(
                                                    possible_inventory_choices[player_inventory_item_selected])
                                                player_info["breastplate"] = armor_new_equipped
                                                self.showMessage(Constants.PLAYER_INVENTORY_NEW_ARMOR_EQUIPPED)
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                return self.manageInventory()
                                            elif player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_NO:
                                                break
                                            else:
                                                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)
                                        break
                                    elif player_info["chausses"]:
                                        self.showMessage(Constants.PLAYER_INVENTORY_ALREADY_HAS_ARMOR)
                                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                        player_inventory_replace_armor_choice = self.getPlayerChoice()
                                        while True:
                                            if player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_YES:
                                                player_info["backpack_items"]["armors"].append(player_info["chausses"])
                                                armor_new_equipped = possible_inventory_choices[player_inventory_item_selected]
                                                player_info["backpack_items"]["armors"].remove(
                                                    possible_inventory_choices[player_inventory_item_selected])
                                                player_info["chausses"] = armor_new_equipped
                                                self.showMessage(Constants.PLAYER_INVENTORY_NEW_ARMOR_EQUIPPED)
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                return self.manageInventory()
                                            elif player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_NO:
                                                break
                                            else:
                                                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)
                                        break
                                    elif player_info["gauntlets"]:
                                        self.showMessage(Constants.PLAYER_INVENTORY_ALREADY_HAS_ARMOR)
                                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                        player_inventory_replace_armor_choice = self.getPlayerChoice()
                                        while True:
                                            if player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_YES:
                                                player_info["backpack_items"]["armors"].append(player_info["gauntlets"])
                                                armor_new_equipped = possible_inventory_choices[player_inventory_item_selected]
                                                player_info["backpack_items"]["armors"].remove(
                                                    possible_inventory_choices[player_inventory_item_selected])
                                                player_info["gauntlets"] = armor_new_equipped
                                                self.showMessage(Constants.PLAYER_INVENTORY_NEW_ARMOR_EQUIPPED)
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                return self.manageInventory()
                                            elif player_inventory_replace_armor_choice in Constants.PLAYER_PROMPT_SET_FOR_NO:
                                                break
                                            else:
                                                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)
                                        break
                                else:
                                    self.showMessage(Constants.PLAYER_INVENTORY_CANNOT_EQUIP_ITEM)
                        elif player_inventory_selected_item_action_choice == Constants.PLAYER_INVENTORY_ACTION_SET_USE:  # usa un item
                            if possible_inventory_choices[player_inventory_item_selected].item_type == "potion":
                                if player_info["backpack_items"]["potions"][int(player_inventory_item_selected) - 1].name == Item.PotionHealingSmall.name:
                                    if (Player.health + Item.PotionHealingSmall.dmg) >= Player.max_health:
                                        player_info["backpack_items"]["potions"].remove(
                                            possible_inventory_choices[player_inventory_item_selected])
                                        Player.health = Player.max_health
                                        self.showCombinedMessage(Constants.PLAYER_HEALS_MESSAGE,
                                                                     Item.PotionHealingSmall.dmg,
                                                                     Constants.ACRONYM_MESSAGE_HP)
                                    elif Player.health == Player.max_health:
                                        self.showMessage(Constants.PLAYER_CANNOT_HEAL_MESSAGE)
                                    else:
                                        player_info["backpack_items"]["potions"].remove(
                                            possible_inventory_choices[player_inventory_item_selected])
                                        Player.health = Player.health + Item.PotionHealingSmall.dmg
                                        self.showCombinedMessage(Constants.PLAYER_HEALS_MESSAGE,
                                                                 Item.PotionHealingSmall.dmg,
                                                                 Constants.ACRONYM_MESSAGE_HP)
                                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                    return self.manageInventory()
                                elif player_info["backpack_items"]["potions"][int(player_inventory_item_selected) - 1].name == Item.PotionManaSmall.name:
                                    if (Player.mana + Item.PotionManaSmall.dmg) >= Player.max_mana:
                                        player_info["backpack_items"]["potions"].remove(
                                            possible_inventory_choices[player_inventory_item_selected])
                                        Player.mana = Player.max_mana
                                        self.showCombinedMessage(Constants.PLAYER_RESTORES_MANA_MESSAGE,
                                                                     Item.PotionManaSmall.dmg,
                                                                     Constants.ACRONYM_MESSAGE_SK)
                                    elif Player.mana == Player.max_mana:
                                        self.showMessage(Constants.PLAYER_CANNOT_RESTORE_MANA_MESSAGE)
                                    else:
                                        player_info["backpack_items"]["potions"].remove(
                                            possible_inventory_choices[player_inventory_item_selected])
                                        Player.mana = Player.mana + Item.PotionManaSmall.dmg
                                        self.showCombinedMessage(Constants.PLAYER_RESTORES_MANA_MESSAGE,
                                                                 Item.PotionManaSmall.dmg,
                                                                 Constants.ACRONYM_MESSAGE_SK)
                                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                    return self.manageInventory()
                        else:
                            self.showWarning(Constants.WARNING_MESSAGE_INVALID_INVENTORY_ITEM_ACTION)
                else:
                    self.showWarning(Constants.WARNING_MESSAGE_PLAYER_HAS_NO_ITEMS_TO_CHANGE)
            elif player_inventory_action_choice in Constants.PLAYER_PROMPT_TO_RETURN:
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                if battle:
                    return
                return self.idleState()
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_INVENTORY_ACTION)

    def shopping(self, shop_classobj):
        print("no fuimo de choppin")
        self.waitForButtonPress()
        return self.idleState()

    def gameOver(self):
        self.clearScreen()
        self.showMessage(Constants.PLAYER_DIED)
        self.showMessage(Constants.GAME_OVER)
        while True:
            player_game_over_option_choice = self.getPlayerChoice()
            if player_game_over_option_choice == "1":
                self.loadGame()
                return self.idleState()
            elif player_game_over_option_choice == "2":
                return exit(0)
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_GAME_OVER_SCREEN_OPTION)

    def battle(self, enemy, risk):
        global Player
        global player_info
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showCombinedMessage(Constants.SOMEONE_IS_ENEMY, enemy.name,Constants.SOMEONE_IS_ENEMY_AND_READY_TO_ATTACK)
        enemy_max_health = enemy.health
        while True:
            if Player.mana <= 0:
                self.showCombinedMessage("\n"+enemy.name, "\n"+f"Hp: {enemy.health}/{enemy_max_health}"+"\n\n")
                self.showCombinedMessage(Player.name, "\n"+f"Hp: {Player.health:.2f}/{Player.max_health}", "\n"+f"Sk: 0/{Player.max_mana}"+"\n\n")
                self.showMessage(Constants.COMBAT_OPTIONS)
            else:
                self.showCombinedMessage("\n"+enemy.name, "\n"+f"Hp: {enemy.health}/{enemy_max_health}"+"\n\n")
                self.showCombinedMessage(Player.name, "\n"+f"Hp: {Player.health:.2f}/{Player.max_health}", "\n"+f"Sk: {Player.mana}/{Player.max_mana}"+"\n\n")
                self.showMessage(Constants.COMBAT_OPTIONS)
            while True:
                player_battle_option_choice = self.getPlayerChoice()
                if player_battle_option_choice == "1":
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showCombinedMessage(Player.name, Constants.SOMEONE_ATTACKS)
                    enemy_current_health = enemy.health
                    if enemy.takeDamageFromPlayerCommon(Player, player_info):
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        return self.givePlayerRewardAfterVictory(enemy, risk)
                    else:
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        if enemy_current_health != enemy.health:
                            self.showCombinedMessage(enemy.name, Constants.SOMEONE_RECEIVES_DAMAGE, (enemy_current_health - enemy.health),"\n")
                            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                            self.showCombinedMessage(enemy.name, Constants.SOMEONE_ATTACKS)
                            if enemy.attack(Player):
                                return self.gameOver()
                            else:
                                self.showCombinedMessage(Player.name, Constants.SOMEONE_RECEIVES_DAMAGE, enemy.dmg, "\n")
                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        else:
                            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                            self.showCombinedMessage(enemy.name, Constants.SOMEONE_ATTACKS)
                            if enemy.attack(Player):
                                return self.gameOver()
                            else:
                                self.showCombinedMessage(Player.name, Constants.SOMEONE_RECEIVES_DAMAGE, enemy.dmg, "\n")
                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        break
                elif player_battle_option_choice == "2":
                    if Player.mana <= 0:
                        self.showWarning(Constants.PLAYER_IS_OUT_OF_MANA)
                        continue
                    else:
                        self.showMessage(Player.getSpecialAttackOptions())
                        while True:
                            player_special_attack_choice = self.getPlayerChoice()
                            if player_special_attack_choice == "1":
                                self.showMessage(Player.getSpecialAttackDescription())
                                self.showMessage(Constants.SPECIAL_ATTACK_CONFIRM)
                                while True:
                                    player_special_attack_choice_confirmation = self.getPlayerChoice()
                                    if player_special_attack_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_YES:
                                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                        self.showCombinedMessage(Player.name, Constants.SOMEONE_ATTACKS)
                                        enemy_current_health = enemy.health
                                        if enemy.takeDamageFromPlayerSpecial(Player, player_info):
                                            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                            return self.givePlayerRewardAfterVictory(enemy, risk)
                                        else:
                                            if enemy_current_health != enemy.health:
                                                self.showCombinedMessage(enemy.name,
                                                                         Constants.SOMEONE_RECEIVES_DAMAGE,
                                                                         (enemy_current_health - enemy.health), "\n")
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                self.showCombinedMessage(enemy.name, Constants.SOMEONE_ATTACKS)
                                                if enemy.attack(Player):
                                                    return self.gameOver()
                                                else:
                                                    self.showCombinedMessage(Player.name,
                                                                             Constants.SOMEONE_RECEIVES_DAMAGE,
                                                                             enemy.dmg, "\n")
                                                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                            else:
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                                self.showCombinedMessage(enemy.name, Constants.SOMEONE_ATTACKS)
                                                if enemy.attack(Player):
                                                    return self.gameOver()
                                                else:
                                                    self.showCombinedMessage(Player.name,
                                                                             Constants.SOMEONE_RECEIVES_DAMAGE,
                                                                             enemy.dmg, "\n")
                                                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                                            break
                                    elif player_special_attack_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                                        break
                                    else:
                                        self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)
                                break
                            else:
                                self.showWarning(Constants.WARNING_MESSAGE_INVALID_SPECIAL_ATTACK)
                        break
                elif player_battle_option_choice == "3":
                    self.manageInventory(False, True)
                    break
                elif player_battle_option_choice == "4":
                    if self.calculateChance(90):
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        self.showCombinedMessage(Player.name, Constants.SOMEONE_FLED)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        self.showMessage(Constants.SOMEONE_FLED_AND_SUCCEEDED)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        return self.idleState()
                    else:
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        self.showCombinedMessage(Player.name, Constants.SOMEONE_FLED)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                        self.showMessage(Constants.SOMEONE_FLED_AND_FAILED)
                        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    break

    def givePlayerRewardAfterVictory(self, enemy, risk):
        global player_info
        global Player
        if risk == "low":  # player will earn between 20 and 90 gold
            money_amount = str(random.randint(20, 90))
            self.showCombinedMessage(enemy.name,
                                     Constants.SOMEONE_IS_DEFEATED,
                                     Constants.PLAYER_WINS,
                                     Constants.PLAYER_EARNS_MONEY_START,
                                     str(money_amount),
                                     Constants.PLAYER_EARNS_MONEY_END)
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            Player.money = money_amount
        elif risk == "medium":  # player will earn between 100 and 180 gold
            money_amount = random.randint(100, 180)
            self.showCombinedMessage(enemy.name,
                                     Constants.SOMEONE_IS_DEFEATED,
                                     Constants.PLAYER_WINS,
                                     Constants.PLAYER_EARNS_MONEY_START,
                                     str(money_amount),
                                     Constants.PLAYER_EARNS_MONEY_END)
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            Player.money = money_amount
        elif risk == "high":  # player will earn between 230 and 300 gold
            money_amount = random.randint(230, 300)
            self.showCombinedMessage(enemy.name,
                                     Constants.SOMEONE_IS_DEFEATED,
                                     Constants.PLAYER_WINS,
                                     Constants.PLAYER_EARNS_MONEY_START,
                                     str(money_amount),
                                     Constants.PLAYER_EARNS_MONEY_END)
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            Player.money = money_amount
        return self.idleState()

    def createCharacter(self):
        global player_info
        global Player
        # método que es llamado al elegir "nuevo juego" en el menu principal
        # el usuario podrá crear su personaje y elegir su spawnpoint
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_NAME_MESSAGE)
        while True:
            # while para prevenir que el usuario ingrese un nombre no válido
            player_name = self.getPlayerChoice(Constants.PLAYER_PROMPT_NAME)
            if player_name.isalpha():
                break
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_NAME)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_CLASS_MESSAGE)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        while True:
            # while principal para prevenir que el usuario ingrese una clase o carácter no válido/a
            player_class_choice = self.getPlayerChoice()
            # se le asigna a una variable porque si no estaría preguntando "Opción: " una y otra vez en cada elif
            if player_class_choice == "1":      # Opción 1 corresponde a Arquero
                # Cl_Archer se refiere al módulo y .Archer a la clase. Esto aplica para los otros player_class_choice.
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_ARCHER,
                                                                Cl_Archer.Archer(player_name))
                # si el usuario ingresó si, entonces variable player existe y es instancia. De lo contrario será None.
                if Player:
                    # este chequeo no es función, ya que no hay forma de retornar un break o continue
                    player_info = {"weapon_1": Item.BowNewborn,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "2":    # Opción 2 corresponde a Mago
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WIZARD,
                                                                Cl_Wizard.Wizard(player_name))
                if Player:
                    player_info = {"weapon_1": Item.ElementaryCharity,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "3":    # Opción 3 corresponde a Guerrero
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_WARRIOR,
                                                                Cl_Warrior.Warrior(player_name))
                if Player:
                    player_info = {"weapon_1": Item.WolfSword,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "4":    # Opción 4 corresponde a Ladrón
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_THIEF,
                                                                Cl_Thief.Thief(player_name))
                if Player:
                    player_info = {"weapon_1": Item.PhoenixDagger,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "5":    # Opción 5 corresponde a Hechicero
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_SORCERER,
                                                                Cl_Sorcerer.Sorcerer(player_name))
                if Player:
                    player_info = {"weapon_1": Item.MagickBook,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "6":    # Opción 6 corresponde a Paladin
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_PALADIN,
                                                                Cl_Paladin.Paladin(player_name))
                if Player:
                    player_info = {"weapon_1": Item.HolySword,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "7":    # Opción 7 corresponde a Nigromante
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_NECROMANCER,
                                                                Cl_Necro.Necromancer(player_name))
                if Player:
                    player_info = {"weapon_1": Item.SoulBlinder,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "8":    # Opción 8 corresponde a Tanque
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_TANK,
                                                                Cl_Tank.Tank(player_name))
                if Player:
                    player_info = {"weapon_1": Item.RapthaliaShield,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            elif player_class_choice == "9":    # Opción 9 corresponde a Bardo
                Player = self.confirmPlayerClassChoiceAndAssign(Constants.CHARACTER_CREATION_DESCRIPTION_BARD,
                                                                Cl_Bard.Bard(player_name))
                if Player:
                    player_info = {"weapon_1": Item.MiraculousHarp,
                                   "helmet": False,
                                   "breastplate": False,
                                   "chausses": False,
                                   "gauntlets": False,
                                   "backpack_items": {"weapons": [],
                                                      "potions": [],
                                                      "armors": []},
                                   "location": None}
                    break
                else:
                    self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                    self.showMessage(Constants.CHARACTER_CREATION_ALL_CLASSES)
                    continue
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_CLASS)
        del player_class_choice
        del player_name
        # se eliminan de memoria las variables que ya no harán falta por el resto de la ejecución del juego
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_WORLD_MESSAGE)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_WORLD_SPAWNPOINTS)
        while True:
            player_spawnpoint_choice = self.getPlayerChoice()
            self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
            if player_spawnpoint_choice == "1":     # Opción 1 Corresponde a Muldraugh
                if self.confirmPlayerSpawnpoint(POI.Muldraugh):
                    break
                else:
                    continue
            elif player_spawnpoint_choice == "2":   # Opción 2 corresponde a Riverside
                if self.confirmPlayerSpawnpoint(POI.Riverside):
                    break
                else:
                    continue
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_SPAWNPOINT_CHOICE)

        return self.saveGame()

    def confirmPlayerClassChoiceAndAssign(self, class_description, classrpg_with_player_name_classobj):
        #
        # Método verifica que el usuario elige a la clase descrita, asegurando una respuesta esperada ("si" o "no")
        # <constante de descripción de la clase correspondiente a player_class_choice> pasada como primer argumento,
        # por ejemplo la constante Constantes.CHARACTER_DESCRIPTION_ARCHER
        #
        # Método devuelve la clase a asignar a la variable <player> (fuera de este método) si el usuario elige "si"
        # (la clase a asignar es pasada como segundo argumento, debe ser paquete.módulo(<variable del nombre
        # del jugador>) donde esa <variable del nombre> es pasada como argumento para el constructor de la clase
        # que se requiera, por ejemplo Archer.Archer(player_name)
        # También se puede decir que este método devuelve el segundo argumento para instanciar dicho argumento (clase)
        #
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(class_description)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_CLASS_CONFIRM)
        while True:
            # while para prevenir que usuario escriba otra cosa que no sea "si" o "no" cuando confirma su clase
            player_class_choice_confirmation = self.getPlayerChoice()
            if player_class_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_YES:
                return classrpg_with_player_name_classobj
            elif player_class_choice_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                return None
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)

    def confirmPlayerSpawnpoint(self, location_classobj):
        global player_info
        self.showCombinedMessage("\n" + location_classobj.name, "\n" + location_classobj.description)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
        self.showMessage(Constants.CHARACTER_CREATION_WORLD_SPAWNPOINT_CONFIRMATION)
        while True:
            player_spawnpoint_choice_confirm = self.getPlayerChoice()
            if player_spawnpoint_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_YES:
                player_info["location"] = location_classobj
                return True
            elif player_spawnpoint_choice_confirm in Constants.PLAYER_PROMPT_SET_FOR_NO:
                self.showMessage(Constants.CHARACTER_CREATION_WORLD_SPAWNPOINTS)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                return False
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)

    def checkIfPlayerIsInLocation(self, location_classobj):
        global player_info
        if player_info["location"].name == location_classobj.name:
            return True
        else:
            return False

    def confirmPlayerSaveFileDeletion(self):
        self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_ALREADY_EXISTS)
        self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_DELETE_CONFIRMATION)
        while True:
            player_delete_savefile_confirmation = self.getPlayerChoice()
            if player_delete_savefile_confirmation in Constants.PLAYER_PROMPT_SET_FOR_YES:
                os.remove("savefile.pickle")
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_DELETED)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                return True
            elif player_delete_savefile_confirmation in Constants.PLAYER_PROMPT_SET_FOR_NO:
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.showMessage(Constants.MAIN_MENU_MESSAGE_SAVEFILE_NOT_DELETED_GOING_BACK_TO_MENU)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.waitSeconds(Constants.TIME_BETWEEN_MESSAGES)
                self.clearScreen()
                return False
            else:
                self.showWarning(Constants.WARNING_MESSAGE_INVALID_YES_OR_NO_CONFIRMATION)

    def calculateChance(self, chance):
        # Devolverá un valor booleano, random.random() devuelve un flotante cualquiera
        # Por ej. 0.619374830802 el cual es menor (<) a 0.80 (es decir 80/100)
        # Por ej2: si quiero saber si algo ocurre con un 80% de chance, simplemente ingresar 80 como argumento
        if random.random() < (chance / 100):
            return True
        else:
            return False

    def getPlayerChoice(self, prompt=Constants.PLAYER_PROMPT_OPTION):
        # por defecto hará input("Opción: "), ingresar argumento para cambiar el mensaje
        return input(prompt)

    def saveGame(self):
        global player_info
        global Player
        with open("savefile.pickle", "wb") as f:
            pickle.dump(player_info, f, protocol=0)
            pickle.dump(Player, f, protocol=0)
            f.close()
        with open("savefile.pickle", "rb") as f:
            player_info = pickle.load(f)
            Player = pickle.load(f)
            f.close()
        return None

    def loadGame(self):
        global player_info
        global Player
        with open("savefile.pickle", "rb") as f:
            player_info = pickle.load(f)
            Player = pickle.load(f)
            f.close()
        return None

    def clearScreen(self):
        return os.system("cls")

    def showMessage(self, message):
        # Mostrará por pantalla la cadena pasada como argumento
        return print(message)

    def showCombinedMessage(self, msg1, msg2, msg3="", msg4="", msg5="",
                            msg6="", msg7="", msg8="", msg9="", msg10=""):
        return print(msg1, msg2, msg3, msg4, msg5,
                     msg6, msg7, msg8, msg9, msg10)

    def showWarning(self, message):
        self.showMessage("\n"+message)
        self.waitSeconds(Constants.TIME_BETWEEN_WARNINGS)
        #
        # A continuación se hace uso de Secuencias de Escape, Secuencias de códigos de Escape y Secuencias de Control
        #
        # - El carácter ESC (como si estuviéramos apretando esa tecla) se llama carácter de control.
        # - Barra \ en python (y específicamente en C) es el "carácter de escape", se usa para indicar que
        #   la siguiente letra debe ser interpretada de otra forma, esto permite controlar la salida en pantalla,
        #   es decir, el standard output. Esto incluye nueva linea (\n), eliminar una linea (carriage return: \r),
        #   tabulación (\t), entre otros.
        #
        # ° Secuencias de escape utilizadas: \033 y \x1b.
        #   - El primero usa el sistema octal. Para utilizar el sistema octal se debe hacer uso
        #     del carácter de escape (\) con tres números consecuentes (ej. \000, \033, \127).
        #   - En el código ASCII (googlear tabla), el carácter de control ESC en valores octales es 033.
        #   - Por otro lado, \x1b utiliza hexadecimal, para usar hexadecimal se debe escribir \x con dos números que le
        #     sigan a la x sin espacios. \x1b o \x1B también entonces hacen referencia al carácter de control ESC.
        #   - Extra: el carácter de control ESC en Unicode es \u001b
        #   - Aclaración: no hay una razón específica por la cual se usó dos sistemas distintos en up y clear, fue
        #     simplemente una decisión para que quede más claro cómo funcionan las secuencias. Tranquilamente los dos
        #     podrían usar solamente \x1B o solamente \003.
        #
        # ° Códigos de escape utilizados: [1A y [2K.
        #   - Existen muchos códigos de escape y llevan a cabo una función distinta (por ej. [#A, [#B, [s, [J, etc.
        #     donde # es el argumento y puede ir cualquier número)
        #   - En este caso, [1A indica que el cursor se desplace un lugar arriba. Por tanto [2A indicará que se desplace
        #     2 lugares arriba. Si no se especifica ningún valor simplemente se moverá 1 lugar arriba.
        #   - Para el caso de [2K, indica que se borre la línea entera en donde está parado el cursor. [1k borraría solo
        #     hasta el principio de la línea, y [0K, borraría solo hasta el final de la línea.
        #   - Se llaman así porque se escriben después del carácter de control ESC, es decir \x1B (o \033, o tmb \u001b)

        # ° Secuencias de control (o Secuencias de código de escape) utilizadas: \033[1A y \x1B[2K.
        #   - No son más que las secuencias de escape + los códigos escape en una misma cadena. Fueron guardados en
        #     variables para que sea más claro de entender lo que hacen.
        #   - Para saber más buscar CSI (Control Sequence Introducer)
        #
        #  Por último, el código debajo de este comentario hace lo siguiente: en un print, por defecto, el end= no se ve
        #  y hace que el cursor se pare en la línea debajo del texto que se acaba de mostrar por pantalla,
        #  por lo que si escribimos print("hola") el cursor no va a quedarse en "hola", va a quedarse
        #  en la línea debajo de hola. Al escribir print("hola", end={algo}), estamos especificando qué queremos
        #  que el interpretador haga después de printear, por lo tanto, si escribimos print("hola", end=up), el cursor
        #  ahora SÍ va a estar parado en la misma línea que hola. Con un ejemplo:
        #   print("hola")
        #   time.sleep(1)
        #   print(up, clear)
        #  Esto mostrará "hola" por un segundo, el cursor se moverá arriba en la misma línea que "hola", y la eliminará.
        #
        # Por eso, al mostrar un WARNING_MESSAGE, primero se eliminará el mensaje de advertencia, luego se eliminará el
        # espacio en blanco añadido con \n en ("\n"+message), y por último se eliminará el mensaje de "Opción:" o
        # "Nombre:" ya que se va a mostrar de nuevo de todas formas cuando termine de ejecutarse esta función.
        #
        up = '\033[1A'  # secuencia de control que mueve el cursor 1 línea arriba
        clear = '\x1B[2K'   # secuencia de control que elimina la línea entera en donde el cursor esté parado
        print(up, end=clear)    # eliminará el mensaje de advertencia
        print(up, end=clear)    # eliminará la nueva línea anidada al mensaje de advertencia (es decir el \n)
        return print(up, end=clear)  # eliminará el mensaje para el usuario "Opción:" o "Nombre:" o cualquier otro

    def waitSeconds(self, seconds):
        time.sleep(seconds)
        return None

    def waitForButtonPress(self, message=Constants.PRESS_ENTER_TO_CONTINUE):
        return input(message)


# Testeando
# print(Constants.player_inv["weapon_1"])
# Constants.player_inv["weapon_1"] = "Espada de Tenshi"

# manager = GameManager()
# manager.waitForButtonPress()
# print(Constants.COMBAT_OPTIONS)
