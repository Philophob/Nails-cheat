import os
import pymem
import pymem.process
import keyboard
import time
import math
import re


# offsets

cs_gamerules_data = 0x0;
m_ArmorValue = 0x117CC;
m_Collision = 0x320;
m_CollisionGroup = 0x474;
m_Local = 0x2FCC;
m_MoveType = 0x25C;
m_OriginalOwnerXuidHigh = 0x31D4;
m_OriginalOwnerXuidLow = 0x31D0;
m_SurvivalGameRuleDecisionTypes = 0x1328;
m_SurvivalRules = 0xD00;
m_aimPunchAngle = 0x303C;
m_aimPunchAngleVel = 0x3048;
m_angEyeAnglesX = 0x117D0;
m_angEyeAnglesY = 0x117D4;
m_bBombDefused = 0x29C0;
m_bBombPlanted = 0x9A5;
m_bBombTicking = 0x2990;
m_bFreezePeriod = 0x20;
m_bGunGameImmunity = 0x9990;
m_bHasDefuser = 0x117DC;
m_bHasHelmet = 0x117C0;
m_bInReload = 0x32B5;
m_bIsDefusing = 0x997C;
m_bIsQueuedMatchmaking = 0x74;
m_bIsScoped = 0x9974;
m_bIsValveDS = 0x7C;
m_bSpotted = 0x93D;
m_bSpottedByMask = 0x980;
m_bStartedArming = 0x3400;
m_bUseCustomAutoExposureMax = 0x9D9;
m_bUseCustomAutoExposureMin = 0x9D8;
m_bUseCustomBloomScale = 0x9DA;
m_clrRender = 0x70;
m_dwBoneMatrix = 0x26A8;
m_fAccuracyPenalty = 0x3340;
m_fFlags = 0x104;
m_flC4Blow = 0x29A0;
m_flCustomAutoExposureMax = 0x9E0;
m_flCustomAutoExposureMin = 0x9DC;
m_flCustomBloomScale = 0x9E4;
m_flDefuseCountDown = 0x29BC;
m_flDefuseLength = 0x29B8;
m_flFallbackWear = 0x31E0;
m_flFlashDuration = 0x10470;
m_flFlashMaxAlpha = 0x1046C;
m_flLastBoneSetupTime = 0x2928;
m_flLowerBodyYawTarget = 0x9ADC;
m_flNextAttack = 0x2D80;
m_flNextPrimaryAttack = 0x3248;
m_flSimulationTime = 0x268;
m_flTimerLength = 0x29A4;
m_hActiveWeapon = 0x2F08;
m_hBombDefuser = 0x29C4;
m_hMyWeapons = 0x2E08;
m_hObserverTarget = 0x339C;
m_hOwner = 0x29DC;
m_hOwnerEntity = 0x14C;
m_hViewModel = 0x3308;
m_iAccountID = 0x2FD8;
m_iClip1 = 0x3274;
m_iCompetitiveRanking = 0x1A84;
m_iCompetitiveWins = 0x1B88;
m_iCrosshairId = 0x11838;
m_iDefaultFOV = 0x333C;
m_iEntityQuality = 0x2FBC;
m_iFOV = 0x31F4;
m_iFOVStart = 0x31F8;
m_iGlowIndex = 0x10488;
m_iHealth = 0x100;
m_iItemDefinitionIndex = 0x2FBA;
m_iItemIDHigh = 0x2FD0;
m_iMostRecentModelBoneCounter = 0x2690;
m_iObserverMode = 0x3388;
m_iShotsFired = 0x103E0;
m_iState = 0x3268;
m_iTeamNum = 0xF4;
m_lifeState = 0x25F;
m_nBombSite = 0x2994;
m_nFallbackPaintKit = 0x31D8;
m_nFallbackSeed = 0x31DC;
m_nFallbackStatTrak = 0x31E4;
m_nForceBone = 0x268C;
m_nTickBase = 0x3440;
m_nViewModelIndex = 0x29D0;
m_rgflCoordinateFrame = 0x444;
m_szCustomName = 0x304C;
m_szLastPlaceName = 0x35C4; 
m_thirdPersonViewAngles = 0x31E8;
m_vecOrigin = 0x138;
m_vecVelocity = 0x114;
m_vecViewOffset = 0x108;
m_viewPunchAngle = 0x3030;
m_zoomLevel = 0x33E0;
anim_overlays = 0x2990;
clientstate_choked_commands = 0x4D30;
clientstate_delta_ticks = 0x174;
clientstate_last_outgoing_command = 0x4D2C;
clientstate_net_channel = 0x9C;
convar_name_hash_table = 0x2F0F8;
dwClientState = 0x589FCC;
dwClientState_GetLocalPlayer = 0x180;
dwClientState_IsHLTV = 0x4D48;
dwClientState_Map = 0x28C;
dwClientState_MapDirectory = 0x188;
dwClientState_MaxPlayer = 0x388;
dwClientState_PlayerInfo = 0x52C0;
dwClientState_State = 0x108;
dwClientState_ViewAngles = 0x4D90;
dwEntityList = 0x4DC179C;
dwForceAttack = 0x31F1CB4;
dwForceAttack2 = 0x31F1CC0;
dwForceBackward = 0x31F1CFC;
dwForceForward = 0x31F1D08;
dwForceJump = 0x526B5B0;
dwForceLeft = 0x31F1D20;
dwForceRight = 0x31F1D14;
dwGameDir = 0x628700;
dwGameRulesProxy = 0x52DE88C;
dwGetAllClasses = 0xDCFAB4;
dwGlobalVars = 0x589CD0;
dwGlowObjectManager = 0x5309C78;
dwInput = 0x5212D60;
dwInterfaceLinkList = 0x957AA4;
dwLocalPlayer = 0xDA747C;
dwMouseEnable = 0xDACFC8;
dwMouseEnablePtr = 0xDACF98;
dwPlayerResource = 0x31F0040;
dwRadarBase = 0x51F6514;
dwSensitivity = 0xDACE64;
dwSensitivityPtr = 0xDACE38;
dwSetClanTag = 0x8A290;
dwViewMatrix = 0x4DB30B4;
dwWeaponTable = 0x5213824;
dwWeaponTableIndex = 0x326C;
dwYawPtr = 0xDACC28;
dwZoomSensitivityRatioPtr = 0xDB1EC8;
dwbSendPackets = 0xD9342;
dwppDirect3DDevice9 = 0xA7050;
find_hud_element = 0x2B5F3080;
force_update_spectator_glow = 0x3B412A;
interface_engine_cvar = 0x3E9EC;
is_c4_owner = 0x3C1090;
m_bDormant = 0xED;
m_flSpawnTime = 0x103C0;
m_pStudioHdr = 0x2950;
m_pitchClassPtr = 0x51F67B0;
m_yawClassPtr = 0xDACC28;
model_ambient_min = 0x58D044;
set_abs_angles = 0x1E3F70;
set_abs_origin = 0x1E3DB0;



# with this you can change the file hash
antivac1 = "85839552263df67e724a2d38519247e2" # change this 
antivac2 = 32740525034503245034873407523400355400100213487323 # change this 
antivac3 = ["af54eae5714cd8107f886b1659f2138e", 2151253|243, 21347631241243, 2159381251235423253215,  2319659126518275608194, 92154361023] # change this 

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
enginepointer = pm.read_int(engine + dwClientState)


glowActive = False
chamsActive = False
rcsActive = False
aimActive = False
wireActive = False

aimfov = 0.8

rgbT = [255, 0, 0]
rgbCT = [0, 0, 255]




ranks = ["Unranked" , 
                "Silver I",
                "Silver II",
                "Silver III",
                "Silver IV",
                "Silver Elite",
                "Silver Elite Master",
                "Gold Nova I",
                "Gold Nova II",
                "Gold Nova III",
                "Gold Nova Master",
                "Master Guardian I",
                "Master Guardian II",
                "Master Guardian Elite",
                "Distinguished Master Guardian",
                "Legendary Eagle",
                "Legendary Eagle Master",
                "Supreme Master First Class",
                "The Global Elite"]


def rankRevealer():
    
        for i in range(0, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_i = pm.read_int(client + dwLocalPlayer)
                if entity_team_id != pm.read_int(entity_i + m_iTeamNum):
                    player_info = pm.read_int(
                        (pm.read_int(engine + dwClientState)) + dwClientState_PlayerInfo)
                    player_info_items = pm.read_int(pm.read_int(player_info + 0x40) + 0xC)
                    info = pm.read_int(player_info_items + 0x28 + (i * 0x34))
                    playerres = pm.read_int(client + dwPlayerResource)
                    rank = None
                    rank = pm.read_int(playerres + m_iCompetitiveRanking + i * 4)

                    if pm.read_string(info + 0x10) != 'GOTV':
                        
                        print("[0x1]: "  + pm.read_string(info + 0x10) + "   -->   " + ranks[rank])
                        print("------------------------------------------------------------------------------------------")




 
def calc_distance(current_x, current_y, new_x, new_y):
    distancex = new_x - current_x
    if distancex < -89:
        distancex += 360
    elif distancex > 89:
        distancex -= 360
    if distancex < 0.0:
        distancex = -distancex
 
    distancey = new_y - current_y
    if distancey < -180:
        distancey += 360
    elif distancey > 180:
        distancey -= 360
    if distancey < 0.0:
        distancey = -distancey
    return distancex, distancey
 


def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < -180:
        viewAngleY += 360
    return viewAngleX, viewAngleY
 
 

def calcangle(localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
    

    delta_x = localpos1 - enemypos1
    delta_y = localpos2 - enemypos2
    delta_z = localpos3 - enemypos3
    hyp = math.sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
    x = math.atan(delta_z / hyp) * 180 / math.pi
    y = math.atan(delta_y / delta_x) * 180 / math.pi
                    
    if delta_x >= 0.0:
        y += 180.0
    return x,y
                
    

def aimbot():
    player = pm.read_int(client + dwLocalPlayer)
    localTeam = pm.read_int(player + m_iTeamNum)
    engine_pointer = pm.read_int(engine + dwClientState)

    target = None
    olddistx = 111111111111
    olddisty = 111111111111

    for i in range(1, 32):
        entity = pm.read_int(client + dwEntityList + i * 0x10)

        if entity:
            try:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_hp = pm.read_int(entity + m_iHealth)
                entity_dormant = pm.read_int(entity + m_bDormant)
                    
            except:
                print("no players...")
                    

            if localTeam != entity_team_id and entity_hp > 0:
                entity_bones = pm.read_int(entity + m_dwBoneMatrix)
                localpos_x_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles)
                localpos_y_angles = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
                localpos1 = pm.read_float(player + m_vecOrigin)
                localpos2 = pm.read_float(player + m_vecOrigin + 4)
                localpos_z_angles = pm.read_float(player + m_vecViewOffset + 0x8)
                localpos3 = pm.read_float(player + m_vecOrigin + 8) + localpos_z_angles
                
                entitypos_x = pm.read_float(entity_bones + 0x30 * 8 + 0xC)
                entitypos_y = pm.read_float(entity_bones + 0x30 * 8 + 0x1C)
                entitypos_z = pm.read_float(entity_bones + 0x30 * 8 + 0x2C)

                X, Y = calcangle(localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z)
                newdist_x, newdist_y = calc_distance(localpos_x_angles, localpos_y_angles, X, Y)
                if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= aimfov and newdist_y <= aimfov:
                    olddistx, olddisty = newdist_x, newdist_y
                    target, target_hp, target_dormant = entity, entity_hp, entity_dormant
                    target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z
            if keyboard.is_pressed("c") and player:
                if target and target_hp > 0 and not target_dormant:
                    x, y = calcangle(localpos1, localpos2, localpos3, target_x, target_y, target_z)
                    normalize_x, normalize_y = normalizeAngles(x, y)

                    pm.write_float(engine_pointer + dwClientState_ViewAngles, normalize_x)
                    pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y)






def main():

    global glowActive
    global chamsActive
    global rcsActive
    global aimActive
    global wireActive
    

    os.system("cls")
    print("Welcome to Nails Beta")
    print("Coded by: Philophob")
    print("Vk: @philophob_ebawit")
    print("Groups: @nails_cheat")
    print("\n \n Hotkeys:")
    print("----------[Hold]----------")
    print("Bhop: Space")
    print("TriggerBot: Shift")
    print("----------[Toggle]----------")
    print("Glow: F1")
    print("Chams visible: F2")
    print("\n \nLogs:")




    while True:
       

        if client and engine and pm:
            try:
                player = pm.read_int(client + dwLocalPlayer)
                engine_pointer = pm.read_int(engine + dwClientState)
                glow_manager = pm.read_int(client + dwGlowObjectManager) 
                crosshairID = pm.read_int(player + m_iCrosshairId) 
                getcrosshairTarget = pm.read_int(client + dwEntityList + (crosshairID - 1) * 0x10)
                immunitygunganme = pm.read_int(getcrosshairTarget + m_bGunGameImmunity)
                localTeam = pm.read_int(player + m_iTeamNum)
                crosshairTeam = pm.read_int(getcrosshairTarget + m_iTeamNum)
            except:
                print("[NB]: on menu")
                time.sleep(1)
                continue
        
        
        if keyboard.is_pressed("space"):
                force_jump = client + dwForceJump
                player = pm.read_int(client + dwLocalPlayer)
                on_ground = pm.read_int(player + m_fFlags)
        

                if player and on_ground and on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.06)
                    pm.write_int(force_jump, 4)
        
        
        

        if keyboard.is_pressed("shift"):
            player = pm.read_int(client + dwLocalPlayer)
            entity_id = pm.read_int(player + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

            entity_team = pm.read_int(entity + m_iTeamNum)
            player_team = pm.read_int(player + m_iTeamNum)

            if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                pm.write_int(client + dwForceAttack, 6)

        
        

        if keyboard.is_pressed("F1") and glowActive == False:
            glowActive = True
            print("[NB]: glow active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F1") and glowActive == True:
            glowActive = False
            print("[NB]: glow no active")
            time.sleep(0.2)

        if(glowActive):
            glowManager = pm.read_int(client + dwGlowObjectManager)

            for i in range(1, 32):

                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if entity:

                    entityTeamID = pm.read_int(entity + m_iTeamNum)
                    entityGlow = pm.read_int(entity + m_iGlowIndex)
                    player = pm.read_int(client + dwLocalPlayer)
                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeamID != playerTeam:
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x8, float(1))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0xC , float(0))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x10, float(0))
                        pm.write_float(glowManager + entityGlow * 0x38 + 0x14, float(1))
                        pm.write_int( glowManager + entityGlow * 0x38 + 0x28, 1 )



    
        

        if keyboard.is_pressed("F2") and chamsActive == False:
            chamsActive = True
            print("[NB]: chams active")
            time.sleep(0.2)
        elif keyboard.is_pressed("F2") and chamsActive == True:
            chamsActive = False
            print("[NB]: chams no active")
            time.sleep(0.2)

        if(chamsActive):
            try:
                #time.sleep(0.001)
                for i in range(32):
                    entity = pm.read_int(client + dwEntityList + i * 0x10)

                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entityTeamID = pm.read_int(entity + m_iTeamNum)
                        entityGlow = pm.read_int(entity + m_iGlowIndex)
                        player = pm.read_int(client + dwLocalPlayer)
                        playerTeam = pm.read_int(player + m_iTeamNum)

                        if (entity_team_id != playerTeam):
                            pm.write_int(entity + m_clrRender, (rgbT[0]))
                            pm.write_int(entity + m_clrRender + 0x1, (rgbT[1]))
                            pm.write_int(entity + m_clrRender + 0x2, (rgbT[2]))
                        
                        
                    else:
                        pass
            except Exception as error:
                print(error)




if __name__ == "__main__":
    main()