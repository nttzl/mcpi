# by nttzl

# 所有方块id的描述
blocks = {0: '空气Air', 1: '石头Stone', (1, 1): '花岗岩Granite', (1, 2): '磨制花岗岩Polished Granite', (1, 3): '闪长岩Diorite', (1, 4): '磨制闪长岩Polished Diorite', (1, 5): '安山岩Andesite', (1, 6): '磨制安山岩Polished Andesite', 2: '草方块Grass', 3: '泥土Dirt', (3, 1): '砂土Coarse Dirt', (3, 2): '灰化土Podzol', 4: '圆石Cobble Stone', 5: '橡木板Oak Wood Plank', (5, 1): '云杉木板Spruce Wood Plank', (5, 2): '桦木板Birch Wood Plank', (5, 3): '丛林中的木板Jungle Wood Plank', (5, 4): '合欢木板Acacia Wood Plank', (5, 5): '深色橡木木板Dark Oak Wood Plank', 6: '橡树树苗Oak Sapling', (6, 1): '云杉树苗Spruce Sapling', (6, 2): '白桦树苗Birch Sapling', (6, 3): '丛林树苗Jungle Sapling', (6, 4): '合欢树苗Acacia Sapling', (6, 5): '深色橡树苗Dark Oak Sapling', 7: '基岩Bedrock', 8: '流水Flowing Water', 9: '水Still Water', 10: '流动的熔岩Flowing Lava', 11: '熔岩Still Lava', 12: '沙子Sand', (12, 1): '红沙Red Sand', 13: '沙砾Gravel', 14: '金矿石Gold Ore', 15: '铁矿石Iron Ore', 16: '煤矿石Coal Ore', 17: '橡木Oak Wood', (17, 1): '云杉木Spruce Wood', (17, 2): '白桦木Birch Wood', (17, 3): '丛林木Jungle Wood', 18: '橡树叶Oak Leaves', (18, 1): '云杉树叶Spruce Leaves', (18, 2): '白桦树叶Birch Leaves', (18, 3): '丛林树叶Jungle Leaves', 19: '海绵Sponge', (19, 1): '湿海绵Wet Sponge', 20: '玻璃Glass', 21: '青金矿石Lapis Lazuli Ore', 22: '青金石块Lapis Lazuli Block', 23: '发射器Dispenser', 24: '沙石Sandstone', (24, 1): '錾制沙石Chiseled Sandstone', (24, 2): '光滑沙石Smooth Sandstone', 25: '音符盒Note Block', 26: '床Bed', 27: '动力铁轨Powered Rail', 28: '探测器的轨道Detector Rail', 29: '黏性活塞Sticky Piston', 30: '蛛网Cobweb', 31: '死灌木Dead Shrub', (31, 1): '草Grass', (31, 2): '蕨类植物Fern', 32: '枯死的灌木Dead Bush', 33: '活塞Piston', 34: '活塞头Piston Head', (35, 0): '白色羊毛White Wool', (35, 1): '橙色羊毛Orange Wool', (35, 2): '品红色羊毛Magenta Wool', (35, 3): '淡蓝色羊毛Light Blue Wool', (35, 4): '黄色羊毛Yellow Wool', (35, 5): '黄绿色羊毛Lime Wool', (35, 6): '粉色羊毛Pink Wool', (35, 7): '灰色羊毛Gray Wool', (35, 8): '浅灰色羊毛Light Gray Wool', (35, 9): '青色羊毛Cyan Wool', (35, 10): '紫色羊毛Purple Wool', (35, 11): '蓝色羊毛Blue Wool', (35, 12): '棕色羊毛Brown Wool', (35, 13): '绿色羊毛Green Wool', (35, 14): '红毛Red Wool', (35, 15): '黑色羊毛Black Wool', 37: '蒲公英Dandelion', 38: '罂粟Poppy', (38, 1): '兰花Blue Orchid', (38, 2): '小花Allium', (38, 3): '茜草花Azure Bluet', (38, 4): '红色郁金香Red Tulip', (38, 5): '橙色郁金香Orange Tulip', (38, 6): '白色郁金香White Tulip', (38, 7): '粉色郁金香Pink Tulip', (38, 8): '雏菊Oxeye Daisy', 39: '棕色蘑菇Brown Mushroom', 40: '红色蘑菇Red Mushroom', 41: '金块Gold Block', 42: '铁块Iron Block', 43: '双层石板Double Stone Slab', (43, 1): '双层沙石板Double Sandstone Slab', (43, 2): '双层木板Double Wooden Slab', (43, 3): '双石子板Double Cobblestone Slab', (43, 4): '双层砖板Double Brick Slab', (43, 5): '双层石砖板Double Stone Brick Slab', (43, 6): '双层末地砖板Double Nether Brick Slab', (43, 7): '双层石英板Double Quartz Slab', 44: '石板Stone Slab', (44, 1): '沙石板Sandstone Slab', (44, 2): '木板Wooden Slab', (44, 3): '圆石台阶Cobblestone Slab', (44, 4): '砖板Brick Slab', (44, 5): '石砖板Stone Brick Slab', (44, 6): '末地砖板Nether Brick Slab', (44, 7): '石英板Quartz Slab', 45: '砖块Bricks', 46: 'TNT', 47: '书架Bookshelf', 48: '苔石Moss Stone', 49: '黑曜石Obsidian', 50: '火把Torch', 51: '火Fire', 52: '刷怪笼Monster Spawner', 53: '橡木台阶Oak Wood Stairs', 54: '箱子Chest', 55: '红石Redstone Wire', 56: '钻石矿Diamond Ore', 57: '钻石块Diamond Block', 58: '工作台Crafting Table', 59: '小麦Wheat Crops', 60: '耕地Farmland', 61: '熔炉Furnace', 62: '燃烧的熔炉Burning Furnace', 63: '木牌Standing Sign Block', 64: '橡木门Oak Door Block', 65: '梯子Ladder', 66: '铁轨ail', 67: '石台阶Cobblestone Stairs', 68: '墙上的木牌Wall-mounted Sign Block', 69: '控制杆Lever', 70: '石质压力板Stone Pressure Plate', 71: '铁门Iron Door Block', 72: '木质压力板Wooden Pressure Plate', 73: '红石矿Redstone Ore', 74: '发光红石矿Glowing Redstone Ore', 75: '红石火把（灭）Redstone Torch (off)', 76: '红石火把（亮）Redstone Torch (on)', 77: '按钮Stone Button', 78: '雪块Snow', 79: '冰Ice', 80: '雪块Snow Block', 81: '仙人掌Cactus', 82: '黏土Clay', 83: '甘蔗Sugar Canes', 84: '唱片机ukebox', 85: '橡木栏Oak Fence', 86: '南瓜Pumpkin', 87: '地狱岩Netherrack', 88: '灵魂沙Soul Sand', 89: '萤石Glowstone', 90: '传送门Nether Portal', 91: "南瓜灯Jack o'Lantern", 92: '蛋糕Cake Block', 93: '红石中继器（关）Redstone Repeater Block (off)', 94: '红石中继器（开）Redstone Repeater Block (on)', 95: '白色染色玻璃White Stained Glass', (95, 1): '橙色染色玻璃Orange Stained Glass', (95, 2): '品红染色玻璃Magenta Stained Glass', (95, 3): '淡蓝色染色玻璃Light Blue Stained Glass', (95, 4): '黄色染色玻璃Yellow Stained Glass', (95, 5): '青柠染色玻璃Lime Stained Glass', (95, 6): '粉色染色玻璃Pink Stained Glass', (95, 7): '灰色染色玻璃Gray Stained Glass', (95, 8): '浅灰染色玻璃Light Gray Stained Glass', (95, 9): '青色染色玻璃Cyan Stained Glass', (95, 10): '紫色染色玻璃Purple Stained Glass', (95, 11): '蓝色染色玻璃Blue Stained Glass', (95, 12): '棕色染色玻璃Brown Stained Glass', (95, 13): '绿色染色玻璃Green Stained Glass', (95, 14): '红色染色玻璃Red Stained Glass', (95, 15): '黑色染色玻璃Black Stained Glass', 96: '木质活版门Wooden Trapdoor', 97: '石头刷怪蛋Stone Monster Egg', (97, 1): '鹅卵石刷怪蛋Cobblestone Monster Egg', (97, 2): '石砖刷怪蛋Stone Brick Monster Egg', (97, 3): '苔石刷怪蛋Mossy Stone Brick Monster Egg', (97, 4): '裂石砖怪物蛋Cracked Stone Brick Monster Egg', (97, 5): '錾制石砖怪物蛋Chiseled Stone Brick Monster Egg', 98: '石砖Stone Bricks', (98, 1): '苔石砖Mossy Stone Bricks', (98, 2): 'Cracked Stone Bricks', (98, 3): 'Chiseled Stone Bricks', 99: '棕色蘑菇Brown Mushroom Block', 100: '红色蘑菇Red Mushroom Block', 101: '铁栏杆Iron Bars', 102: '玻璃板Glass Pane', 103: '西瓜Melon Block', 104: '南瓜苗Pumpkin Stem', 105: '瓜苗Melon Stem', 106: '藤蔓Vines', 107: '橡木篱笆门Oak Fence Gate', 108: '砖台阶Brick Stairs', 109: '石砖台阶Stone Brick Stairs', 110: '菌丝Mycelium', 111: '睡莲Lily Pad', 112: '地狱砖Nether Brick', 113: '地狱砖栅栏Nether Brick Fence', 114: '地狱砖台阶Nether Brick Stairs', 115: '地狱疣Nether Wart', 116: '附魔台Enchantment Table', 117: '酿造台Brewing Stand', 118: '炼药锅Cauldron', 119: 'End Portal', 120: '末地传送门End Portal Frame', 121: '末地石End Stone', 122: '龙蛋Dragon Egg', 123: '红石灯（灭）Redstone Lamp (inactive)', 124: '红石灯（亮）Redstone Lamp (active)', 125: '双层橡木板Double Oak Wood Slab', (125, 1): '双层云杉木板Double Spruce Wood Slab', (125, 2): '双层桦木板Double Birch Wood Slab', (125, 3): '双层丛林木板Double Jungle Wood Slab', (125, 4): '双层合欢木木板Double Acacia Wood Slab', (125, 5): '双层深色橡木板Double Dark Oak Wood Slab', 126: '橡木板Oak Wood Slab', (126, 1): '云杉木板Spruce Wood Slab', (126, 2): '桦木板Birch Wood Slab', (126, 3): '丛林木板Jungle Wood Slab', (126, 4): '合欢木木板Acacia Wood Slab', (126, 5): '深色橡木板Dark Oak Wood Slab', 127: '可可豆Cocoa', 128: '沙石台阶Sandstone Stairs', 129: '绿宝石矿Emerald Ore', 130: '末影箱Ender Chest', 131: '拌线钩Tripwire Hook', 132: '线Tripwire', 133: '绿宝石Emerald Block', 134: '云杉台阶Spruce Wood Stairs', 135: '桦木台阶Birch Wood Stairs', 136: '丛林木台阶Jungle Wood Stairs', 137: '命令方块Command Block', 138: '信标Beacon', 139: '圆石墙Cobblestone Wall', (139, 1): '苔石墙Mossy Cobblestone Wall', 140: '花盆Flower Pot', 141: '红萝卜arrots', 142: '马铃薯Potatoes', 143: '按钮Wooden Button', 144: '骷髅头Mob Head', 145: '铁砧Anvil', 146: '陷阱箱Trapped Chest', 147: '测重压力板（轻）Weighted Pressure Plate (light)', 148: '测重压力板（重）Weighted Pressure Plate (heavy)', 149: '红石比较器（关）Redstone Comparator (inactive)', 150: '红石比较器（开）Redstone Comparator (active)', 151: '阳光感应器Daylight Sensor', 152: '红石块Redstone Block', 153: '下界石英矿Nether Quartz Ore', 154: '漏斗Hopper', 155: '石英块Quartz Block', (155, 1): '錾制石英块Chiseled Quartz Block', (155, 2): '竖纹石英块Pillar Quartz Block', 156: '石英台阶Quartz Stairs', 157: '激活铁轨Activator Rail', 158: '投掷器Dropper', 159: '白色黏土White Stained Clay', (159, 1): '橙色黏土Orange Stained Clay', (159, 2): '品红色黏土Magenta Stained Clay', (159, 3): '淡蓝色黏土Light Blue Stained Clay', (159, 4): '黄色黏土Yellow Stained Clay', (159, 5): '青柠色黏土Lime Stained Clay', (159, 6): '粉色黏土Pink Stained Clay', (159, 7): '灰色黏土Gray Stained Clay', (159, 8): '浅灰色黏土Light Gray Stained Clay', (159, 9): '青色黏土Cyan Stained Clay', (159, 10): '紫色黏土Purple Stained Clay', (159, 11): '蓝色黏土Blue Stained Clay', (159, 12): '棕色黏土Brown Stained Clay', (159, 13): '绿色黏土Green Stained Clay', (159, 14): '红色黏土Red Stained Clay', (159, 15): '黑色黏土Black Stained Clay', 160: '白色玻璃板White Stained Glass Pane', (160, 1): '橙色玻璃板Orange Stained Glass Pane', (160, 2): '品红玻璃板Magenta Stained Glass Pane', (160, 3): '浅蓝色玻璃板Light Blue Stained Glass Pane', (160, 4): '黄色玻璃板Yellow Stained Glass Pane', (160, 5): '青柠色玻璃板Lime Stained Glass Pane', (160, 6): '粉色玻璃板Pink Stained Glass Pane', (160, 7): '灰色玻璃板Gray Stained Glass Pane', (160, 8): '浅灰色玻璃板Light Gray Stained Glass Pane', (160, 9): '青色玻璃板Cyan Stained Glass Pane', (160, 10): '紫色玻璃板Purple Stained Glass Pane', (160, 11): '蓝色玻璃板Blue Stained Glass Pane', (160, 12): '棕色玻璃板Brown Stained Glass Pane', (160, 13): '绿色玻璃板Green Stained Glass Pane', (160, 14): '红色玻璃板Red Stained Glass Pane', (160, 15): '黑色玻璃板Black Stained Glass Pane', 161: '合欢木叶Acacia Leaves', (161, 1): '深色橡木叶Dark Oak Leaves', 162: '合欢木木头Acacia Wood', (162, 1): '深色橡木Dark Oak Wood', 163: '合欢木台阶Acacia Wood Stairs', 164: '深色橡木台阶Dark Oak Wood Stairs', 165: '粘液块Slime Block', 166: '屏障Barrier', 167: '铁质活版门Iron Trapdoor', 168: 'Prismarine', (168, 1): 'Prismarine Bricks', (168, 2): 'Dark Prismarine', 169: '海晶灯Sea Lantern', 170: '干草块Hay Bale', 171: '白色地毯White Carpet', (171, 1): '橙色地毯Orange Carpet', (171, 2): '品红地毯Magenta Carpet', (171, 3): '浅蓝色地毯Light Blue Carpet', (171, 4): '黄色地毯Yellow Carpet', (171, 5): '青柠色地毯Lime Carpet', (171, 6): '粉色地毯Pink Carpet', (171, 7): '灰色地毯Gray Carpet', (171, 8): '浅灰色地毯Light Gray Carpet', (171, 9): '青色地毯Cyan Carpet', (171, 10): '紫色地毯Purple Carpet', (171, 11): '蓝色地毯Blue Carpet', (171, 12): '棕色地毯Brown Carpet', (171, 13): '绿色地毯Green Carpet', (171, 14): '红色地毯Red Carpet', (171, 15): '黑色地毯Black Carpet', 172: '硬化粘土Hardened Clay', 173: '煤块Block of Coal', 174: '浮冰Packed Ice', 175: '向日葵Sunflower', (175, 1): '丁香Lilac', (175, 2): '高草丛Double Tallgrass', (175, 3): '大型蕨Large Fern', (175, 4): '玫瑰丛Rose Bush', (175, 5): '牡丹Peony', 176: '自由站立的旗帜Free-standing Banner', 177: '墙上挂的旗帜Wall-mounted Banner', 178: '反向光传感器Inverted Daylight Sensor', 179: '红砂岩Red Sandstone', (179, 1): '錾制红沙石Chiseled Red Sandstone', (179, 2): '平滑红沙石Smooth Red Sandstone', 180: '红沙石楼梯Red Sandstone Stairs', 181: '双红砂岩板Double Red Sandstone Slab', 182: '红沙石台阶Red Sandstone Slab', 183: '云杉木栅栏门Spruce Fence Gate', 184: '白桦木栅栏门Birch Fence Gate', 185: '丛林木栅栏门Jungle Fence Gate', 186: '深色橡木栅栏门Dark Oak Fence Gate', 187: '金合欢栅栏门Acacia Fence Gate', 188: '云杉木栅栏Spruce Fence', 189: '白桦木栅栏Birch Fence', 190: '丛林木栅栏Jungle Fence', 191: '深色橡木栅栏Dark Oak Fence', 192: '金合欢栅栏Acacia Fence', 193: '云杉门Spruce Door Block', 194: '桦木门Birch Door Block', 195: '丛林木门Jungle Door Block', 196: '金合欢木门Acacia Door Block', 197: '深色橡木门Dark Oak Door Block', 198: '末地蜡End Rod', 199: '合唱的植物Chorus Plant', 200: '紫颂花Chorus Flower', 201: 'Purpur块Purpur Block', 202: 'Purpur柱Purpur Pillar', 203: 'Purpur台阶Purpur Stairs', 204: '双层Purpur板Purpur Double Slab', 205: 'Purpur板Purpur Slab', 206: '末地石砖End Stone Bricks', 207: '甜菜根块Beetroot Block', 208: '草径Grass Path', 209: '末地门End Gateway', 210: '重复命令块Repeating Command Block', 211: '命令链块Chain Command Block', 212: '冰Frosted Ice', 255: '结构块Structure Block', 256: '铁锹Iron Shovel', 257: '铁镐Iron Pickaxe', 258: '铁斧Iron Axe', 259: '打火石Flint and Steel', 260: '苹果Apple', 261: '弓Bow', 262: '箭Arrow', 263: '煤Coal', (263, 1): '木炭Charcoal', 264: '钻石Diamond', 265: '铁锭Iron Ingot', 266: '金锭Gold Ingot', 267: '铁剑Iron Sword', 268: '木剑Wooden Sword', 269: '木锹Wooden Shovel', 270: '木镐Wooden Pickaxe', 271: '木斧Wooden Axe', 272: '石剑Stone Sword', 273: '石锹Stone Shovel', 274: '石镐Stone Pickaxe', 275: '石斧Stone Axe', 276: '钻石剑Diamond Sword', 277: '钻石锹Diamond Shovel', 278: '钻石镐Diamond Pickaxe', 279: '钻石斧Diamond Axe', 280: '木棍Stick', 281: '碗Bowl', 282: '蘑菇煲Mushroom Stew', 283: '金剑Golden Sword', 284: '金锹Golden Shovel', 285: '金镐Golden Pickaxe', 286: '金斧Golden Axe', 287: '线String', 288: '羽毛Feather', 289: '火药Gunpowder', 290: '木锄Wooden Hoe', 291: '石锄Stone Hoe', 292: '铁锄Iron Hoe', 293: '钻石锄Diamond Hoe', 294: '金锄Golden Hoe', 295: '小麦种子Wheat Seeds', 296: '小麦Wheat', 297: '面包Bread', 298: '皮头盔Leather Helmet', 299: '皮革外套Leather Tunic', 300: '皮裤Leather Pants', 301: '皮靴Leather Boots', 302: '链甲头盔Chainmail Helmet', 303: '锁甲胸铠Chainmail Chestplate', 304: '链甲护腿Chainmail Leggings', 305: '链甲靴Chainmail Boots', 306: '铁盔Iron Helmet', 307: '铁胸甲Iron Chestplate', 308: '铁护腿Iron Leggings', 309: '铁靴Iron Boots', 310: '钻石头盔Diamond Helmet', 311: '钻石胸甲Diamond Chestplate', 312: '钻石护腿Diamond Leggings', 313: '钻石靴Diamond Boots', 314: '金头盔Golden Helmet', 315: '金胸甲Golden Chestplate', 316: '金护腿Golden Leggings', 317: '金靴Golden Boots', 318: '燧石Flint', 319: '生猪排Raw Porkchop', 320: '熟猪排Cooked Porkchop', 321: '画板Painting', 322: '金苹果Golden Apple', (322, 1): '附魔金苹果Enchanted Golden Apple', 323: '牌子Sign', 324: '橡木门Oak Door', 325: '桶Bucket', 326: '水桶Water Bucket', 327: '岩浆桶Lava Bucket', 328: '矿车Minecart', 329: '鞍Saddle', 330: '铁门Iron Door', 331: '红石Redstone', 332: '雪球Snowball', 333: '橡木船Oak Boat', 334: '皮革Leather', 335: '牛奶Milk Bucket', 336: '砖Brick', 337: '粘土Clay', 338: '甘蔗Sugar Canes', 339: '纸Paper', 340: '书Book', 341: '粘液球Slimeball', 342: '运输矿车Minecart with Chest', 343: '矿车用炉Minecart with Furnace', 344: '鸡蛋Egg', 345: '方向盘Compass', 346: '钓鱼杆Fishing Rod', 347: '钟Clock', 348: '萤石粉Glowstone Dust', 349: '生鱼Raw Fish', (349, 1): '生鲑鱼Raw Salmon', (349, 2): '小丑鱼Clownfish', (349, 3): '河豚Pufferfish', 350: '熟鱼Cooked Fish', (350, 1): '熟鲑鱼Cooked Salmon', 351: '墨囊Ink Sack', (351, 1): '玫瑰红Rose Red', (351, 2): '仙人掌綠Cactus Green', (351, 3): '可可豆Coco Beans', (351, 4): '青金石Lapis Lazuli', (351, 5): '紫色染料Purple Dye', (351, 6): '青色染料Cyan Dye', (351, 7): '浅灰色的染料Light Gray Dye', (351, 8): '灰色染料Gray Dye', (351, 9): '粉色染料Pink Dye', (351, 10): '黄绿色染料Lime Dye', (351, 11): '蒲公英黄Dandelion Yellow', (351, 12): '淡蓝色的染料Light Blue Dye', (351, 13): '品红色染料Magenta Dye', (351, 14): '橙色染料Orange Dye', (351, 15): '骨粉Bone Meal', 352: '骨头Bone', 353: '糖Sugar', 354: '蛋糕Cake', 355: '床Bed', 356: '红石中继器Redstone Repeater', 357: '饼干Cookie', 358: '地图Map', 359: '剪Shears', 360: '西瓜Melon', 361: '南瓜种子Pumpkin Seeds', 362: '西瓜种子Melon Seeds', 363: '生牛肉Raw Beef', 364: '牛排Steak', 365: '生鸡肉Raw Chicken', 366: '熟鸡肉Cooked Chicken', 367: '腐肉Rotten Flesh', 368: '末影珍珠Ender Pearl', 369: '烈焰棒Blaze Rod', 370: '恶魂之泪Ghast Tear', 371: '金粒Gold Nugget', 372: '地狱疣Nether Wart', 373: '水瓶Potion', 374: '瓶子Glass Bottle', 375: '蜘蛛眼Spider Eye', 376: '发酵蛛眼Fermented Spider Eye', 377: '烈焰粉Blaze Powder', 378: '岩浆膏Magma Cream', 379: '酿造台Brewing Stand', 380: '炼药锅Cauldron', 381: '末影之眼Eye of Ender', 382: '闪烁的西瓜Glistering Melon', (383, 50): '苦力怕蛋Spawn Creeper', (383, 51): '骷髅蛋Spawn Skeleton', (383, 52): '蜘蛛蛋Spawn Spider', (383, 54): '僵尸蛋Spawn Zombie', (383, 55): '史莱姆蛋Spawn Slime', (383, 56): '恶魂蛋Spawn Ghast', (383, 57): '僵尸猪人蛋Spawn Pigman', (383, 58): '末影人蛋Spawn Enderman', (383, 59): '洞穴蜘蛛蛋Spawn Cave Spider', (383, 60): '蠹虫蛋Spawn Silverfish', (383, 61): '烈焰人蛋Spawn Blaze', (383, 62): '岩浆怪蛋Spawn Magma Cube', (383, 65): '蝙蝠蛋Spawn Bat', (383, 66): '女巫蛋Spawn Witch', (383, 67): '末影螨Spawn Endermite', (383, 68): '守护者蛋Spawn Guardian', (383, 69): 'Spawn Shulker', (383, 90): '猪蛋Spawn Pig', (383, 91): '羊蛋Spawn Sheep', (383, 92): '牛蛋Spawn Cow', (383, 93): '鸡蛋Spawn Chicken', (383, 94): '鱿鱼蛋Spawn Squid', (383, 95): '狼蛋Spawn Wolf', (383, 96): '哞菇蛋Spawn Mooshroom', (383, 98): '豹猫蛋Spawn Ocelot', (383, 100): '马蛋Spawn Horse', (383, 101): '兔蛋Spawn Rabbit', (383, 120): '村民蛋Spawn Villager', 384: "附魔瓶Bottle o' Enchanting", 385: '火焰弹Fire Charge', 386: '书与笔Book and Quill', 387: '书Written Book', 388: '绿宝石Emerald', 389: '展示框Item Frame', 390: '花盆Flower Pot', 391: '红萝卜Carrot', 392: '土豆Potato', 393: '熟马铃薯Baked Potato', 394: '毒马铃薯Poisonous Potato', 395: '空地图Empty Map', 396: '金萝卜Golden Carrot', 397: '骷髅头Mob Head (Skeleton)', (397, 1): '凋灵骷髅头Mob Head (Wither Skeleton)', (397, 2): '僵尸头Mob Head (Zombie)', (397, 3): '人头Mob Head (Human)', (397, 4): '苦力怕头Mob Head (Creeper)', (397, 5): '龙首Mob Head (Dragon)', 398: '萝卜钓竿Carrot on a Stick', 399: '下界之星Nether Star', 400: '南瓜饼Pumpkin Pie', 401: '烟花火箭Firework Rocket', 402: '烟火之星Firework Star', 403: '附魔书Enchanted Book', 404: '红石比较器Redstone Comparator', 405: '地狱砖Nether Brick', 406: '下界石英Nether Quartz', 407: 'TNT矿车Minecart with TNT', 408: '漏斗矿车Minecart with Hopper', 409: '海晶砂粒Prismarine Shard', 410: '海晶碎片Prismarine Crystals', 411: '兔肉Raw Rabbit', 412: '烤兔肉Cooked Rabbit', 413: '兔肉煲Rabbit Stew', 414: "兔子脚Rabbit's Foot", 415: '兔子皮Rabbit Hide', 416: '盔甲架Armor Stand', 417: '铁马铠Iron Horse Armor', 418: '金马铠Golden Horse Armor', 419: '钻石马铠Diamond Horse Armor', 420: '拴绳Lead', 421: '命名牌Name Tag', 422: '命令方块矿车Minecart with Command Block', 423: '生羊肉Raw Mutton', 424: '烤羊排Cooked Mutton', 425: '旗帜Banner', 427: '云杉木门Spruce Door', 428: '桦木门Birch Door', 429: '丛林木门Jungle Door', 430: '金合欢木门Acacia Door', 431: '深色橡木门Dark Oak Door', 432: '紫魄果Chorus Fruit', 433: 'Popped Chorus Fruit', 434: '甜菜根Beetroot', 435: '甜菜种子Beetroot Seeds', 436: '甜菜根汤Beetroot Soup', 437: "龙息Dragon's Breath", 438: '喷溅药水Splash Potion', 439: '光灵箭Spectral Arrow', 440: '药箭Tipped Arrow', 441: 'Lingering Potion', 442: '盾Shield', 443: '滑翔翼Elytra', 444: '云杉木船Spruce Boat', 445: '桦木船Birch Boat', 446: '丛林木船Jungle Boat', 447: '合欢木船Acacia Boat', 448: '深色橡木船Dark Oak Boat', 2256: '唱片13 Disc', 2257: '唱片Cat Disc', 2258: '唱片Blocks Disc', 2259: '唱片Chirp Disc', 2260: '唱片Far Disc', 2261: '唱片Mall Disc', 2262: '唱片Mellohi Disc', 2263: '唱片Stal Disc', 2264: '唱片Strad Disc', 2265: '唱片Ward Disc', 2266: '唱片11 Disc', 2267: '唱片Wait Disc'}

# 所有可做为建材的方块
built = {1: '石头Stone', (1, 1): '花岗岩Granite', (1, 2): '磨制花岗岩Polished Granite', (1, 3): '闪长岩Diorite', (1, 4): '磨制闪长岩Polished Diorite', (1, 5): '安山岩Andesite', (1, 6): '磨制安山岩Polished Andesite', 2: '草方块Grass', 3: '泥土Dirt', (3, 1): '砂土Coarse Dirt', (3, 2): '灰化土Podzol', 4: '圆石Cobble Stone', 5: '橡木板Oak Wood Plank', (5, 1): '云杉木板Spruce Wood Plank', (5, 2): '桦木板Birch Wood Plank', (5, 3): '丛林中的木板Jungle Wood Plank', (5, 4): '合欢木板Acacia Wood Plank', (5, 5): '深色橡木木板Dark Oak Wood Plank', 7: '基岩Bedrock', 14: '金矿石Gold Ore', 15: '铁矿石Iron Ore', 16: '煤矿石Coal Ore', 17: '橡木Oak Wood', (17, 1): '云杉木Spruce Wood', (17, 2): '白桦木Birch Wood', (17, 3): '丛林木Jungle Wood', 18: '橡树叶Oak Leaves', (18, 1): '云杉树叶Spruce Leaves', (18, 2): '白桦树叶Birch Leaves', (18, 3): '丛林树叶Jungle Leaves', 19: '海绵Sponge', (19, 1): '湿海绵Wet Sponge', 20: '玻璃Glass', 21: '青金矿石Lapis Lazuli Ore', 22: '青金石块Lapis Lazuli Block', 23: '发射器Dispenser', 24: '沙石Sandstone', (24, 1): '錾制沙石Chiseled Sandstone', (24, 2): '光滑沙石Smooth Sandstone', 25: '音符盒Note Block', 29: '黏性活塞Sticky Piston', 33: '活塞Piston', 35: '羊毛Wool', (35, 1): '橙色羊毛Orange Wool', (35, 2): '品红色羊毛Magenta Wool', (35, 3): '淡蓝色羊毛Light Blue Wool', (35, 4): '黄色羊毛Yellow Wool', (35, 5): '黄绿色羊毛Lime Wool', (35, 6): '粉色羊毛Pink Wool', (35, 7): '灰色羊毛Gray Wool', (35, 8): '浅灰色羊毛Light Gray Wool', (35, 9): '青色羊毛Cyan Wool', (35, 10): '紫色羊毛Purple Wool', (35, 11): '蓝色羊毛Blue Wool', (35, 12): '棕色羊毛Brown Wool', (35, 13): '绿色羊毛Green Wool', (35, 14): '红毛Red Wool', (35, 15): '黑色羊毛Black Wool', 41: '金块Gold Block', 42: '铁块Iron Block', 43: '双层石板Double Stone Slab', (43, 1): '双层沙石板Double Sandstone Slab', (43, 2): '双层木板Double Wooden Slab', (43, 3): '双石子板Double Cobblestone Slab', (43, 4): '双层砖板Double Brick Slab', (43, 5): '双层石砖板Double Stone Brick Slab', (43, 6): '双层末地砖板Double Nether Brick Slab', (43, 7): '双层石英板Double Quartz Slab', 44: '石板Stone Slab', (44, 1): '沙石板Sandstone Slab', (44, 2): '木板Wooden Slab', (44, 3): '圆石台阶Cobblestone Slab', (44, 4): '砖板Brick Slab', (44, 5): '石砖板Stone Brick Slab', (44, 6): '末地砖板Nether Brick Slab', (44, 7): '石英板Quartz Slab', 45: '砖块Bricks', 46: 'TNT', 47: '书架Bookshelf', 48: '苔石Moss Stone', 49: '黑曜石Obsidian', 52: '刷怪笼Monster Spawner', 53: '橡木台阶Oak Wood Stairs', 54: '箱子Chest', 56: '钻石矿Diamond Ore', 57: '钻石块Diamond Block', 58: '工作台Crafting Table', 60: '耕地Farmland', 61: '熔炉Furnace', 62: '燃烧的熔炉Burning Furnace', 67: '石台阶Cobblestone Stairs', 73: '红石矿Redstone Ore', 74: '发光红石矿Glowing Redstone Ore', 80: '雪块Snow Block', 82: '黏土Clay', 84: '唱片机ukebox', 86: '南瓜Pumpkin', 87: '地狱岩Netherrack', 88: '灵魂沙Soul Sand', 89: '萤石Glowstone', 91: "南瓜灯Jack o'Lantern",  95: '白色染色玻璃White Stained Glass', (95, 1): '橙色染色玻璃Orange Stained Glass', (95, 2): '品红染色玻璃Magenta Stained Glass', (95, 3): '淡蓝色染色玻璃Light Blue Stained Glass', (95, 4): '黄色染色玻璃Yellow Stained Glass', (95, 5): '青柠染色玻璃Lime Stained Glass', (95, 6): '粉色染色玻璃Pink Stained Glass', (95, 7): '灰色染色玻璃Gray Stained Glass', (95, 8): '浅灰染色玻璃Light Gray Stained Glass', (95, 9): '青色染色玻璃Cyan Stained Glass', (95, 10): '紫色染色玻璃Purple Stained Glass', (95, 11): '蓝色染色玻璃Blue Stained Glass', (95, 12): '棕色染色玻璃Brown Stained Glass', (95, 13): '绿色染色玻璃Green Stained Glass', (95, 14): '红色染色玻璃Red Stained Glass', (95, 15): '黑色染色玻璃Black Stained Glass', 97: '石头刷怪蛋Stone Monster Egg', (97, 1): '鹅卵石刷怪蛋Cobblestone Monster Egg', (97, 2): '石砖刷怪蛋Stone Brick Monster Egg', (97, 3): '苔石刷怪蛋Mossy Stone Brick Monster Egg', (97, 4): '裂石砖怪物蛋Cracked Stone Brick Monster Egg', (97, 5): '錾制石砖怪物蛋Chiseled Stone Brick Monster Egg', 98: '石砖Stone Bricks', (98, 1): '苔石砖Mossy Stone Bricks', (98, 2): 'Cracked Stone Bricks', (98, 3): 'Chiseled Stone Bricks', 99: '棕色蘑菇Brown Mushroom Block', 100: '红色蘑菇Red Mushroom Block', 103: '西瓜Melon Block', 108: '砖台阶Brick Stairs', 109: '石砖台阶Stone Brick Stairs', 110: '菌丝Mycelium', 112: '地狱砖Nether Brick', 114: '地狱砖台阶Nether Brick Stairs', 116: '附魔台Enchantment Table', 118: '炼药锅Cauldron', 121: '末地石End Stone', 123: '红石灯（灭）Redstone Lamp (inactive)', 124: '红石灯（亮）Redstone Lamp (active)', 125: '双层橡木板Double Oak Wood Slab', (125, 1): '双层云杉木板Double Spruce Wood Slab', (125, 2): '双层桦木板Double Birch Wood Slab', (125, 3): '双层丛林木板Double Jungle Wood Slab', (125, 4): '双层合欢木木板Double Acacia Wood Slab', (125, 5): '双层深色橡木板Double Dark Oak Wood Slab', 126: '橡木板Oak Wood Slab', (126, 1): '云杉木板Spruce Wood Slab', (126, 2): '桦木板Birch Wood Slab', (126, 3): '丛林木板Jungle Wood Slab', (126, 4): '合欢木木板Acacia Wood Slab', (126, 5): '深色橡木板Dark Oak Wood Slab', 128: '沙石台阶Sandstone Stairs', 129: '绿宝石矿Emerald Ore', 130: '末影箱Ender Chest', 133: '绿宝石Emerald Block', 134: '云杉台阶Spruce Wood Stairs', 135: '桦木台阶Birch Wood Stairs', 136: '丛林木台阶Jungle Wood Stairs', 137: '命令方块Command Block', 138: '信标Beacon', 139: '圆石墙Cobblestone Wall', (139, 1): '苔石墙Mossy Cobblestone Wall', 144: '骷髅头Mob Head', 146: '陷阱箱Trapped Chest', 151: '阳光感应器Daylight Sensor', 152: '红石块Redstone Block', 153: '下界石英矿Nether Quartz Ore', 154: '漏斗Hopper', 155: '石英块Quartz Block', (155, 1): '錾制石英块Chiseled Quartz Block', (155, 2): '竖纹石英块Pillar Quartz Block', 156: '石英台阶Quartz Stairs', 158: '投掷器Dropper', 159: '白色黏土White Stained Clay', (159, 1): '橙色黏土Orange Stained Clay', (159, 2): '品红色黏土Magenta Stained Clay', (159, 3): '淡蓝色黏土Light Blue Stained Clay', (159, 4): '黄色黏土Yellow Stained Clay', (159, 5): '青柠色黏土Lime Stained Clay', (159, 6): '粉色黏土Pink Stained Clay', (159, 7): '灰色黏土Gray Stained Clay', (159, 8): '浅灰色黏土Light Gray Stained Clay', (159, 9): '青色黏土Cyan Stained Clay', (159, 10): '紫色黏土Purple Stained Clay', (159, 11): '蓝色黏土Blue Stained Clay', (159, 12): '棕色黏土Brown Stained Clay', (159, 13): '绿色黏土Green Stained Clay', (159, 14): '红色黏土Red Stained Clay', (159, 15): '黑色黏土Black Stained Clay', 160: '白色玻璃板White Stained Glass Pane', (160, 1): '橙色玻璃板Orange Stained Glass Pane', (160, 2): '品红玻璃板Magenta Stained Glass Pane', (160, 3): '浅蓝色玻璃板Light Blue Stained Glass Pane', (160, 4): '黄色玻璃板Yellow Stained Glass Pane', (160, 5): '青柠色玻璃板Lime Stained Glass Pane', (160, 6): '粉色玻璃板Pink Stained Glass Pane', (160, 7): '灰色玻璃板Gray Stained Glass Pane', (160, 8): '浅灰色玻璃板Light Gray Stained Glass Pane', (160, 9): '青色玻璃板Cyan Stained Glass Pane', (160, 10): '紫色玻璃板Purple Stained Glass Pane', (160, 11): '蓝色玻璃板Blue Stained Glass Pane', (160, 12): '棕色玻璃板Brown Stained Glass Pane', (160, 13): '绿色玻璃板Green Stained Glass Pane', (160, 14): '红色玻璃板Red Stained Glass Pane', (160, 15): '黑色玻璃板Black Stained Glass Pane', 161: '合欢木叶Acacia Leaves', (161, 1): '深色橡木叶Dark Oak Leaves', 162: '合欢木木头Acacia Wood', (162, 1): '深色橡木Dark Oak Wood', 163: '合欢木台阶Acacia Wood Stairs', 164: '深色橡木台阶Dark Oak Wood Stairs', 167: '铁质活版门Iron Trapdoor', 168: 'Prismarine', (168, 1): 'Prismarine Bricks', (168, 2): 'Dark Prismarine', 169: '海晶灯Sea Lantern', 170: '干草块Hay Bale', 172: '硬化粘土Hardened Clay', 173: '煤块Block of Coal', 174: '浮冰Packed Ice', 178: '反向光传感器Inverted Daylight Sensor', 179: '红砂岩Red Sandstone', (179, 1): '錾制红沙石Chiseled Red Sandstone', (179, 2): '平滑红沙石Smooth Red Sandstone', 180: '红沙石楼梯Red Sandstone Stairs', 181: '双红砂岩板Double Red Sandstone Slab', 182: '红沙石台阶Red Sandstone Slab', 183: '云杉木栅栏门Spruce Fence Gate', 184: '白桦木栅栏门Birch Fence Gate', 185: '丛林木栅栏门Jungle Fence Gate', 186: '深色橡木栅栏门Dark Oak Fence Gate', 187: '金合欢栅栏门Acacia Fence Gate', 201: 'Purpur块Purpur Block', 202: 'Purpur柱Purpur Pillar', 203: 'Purpur台阶Purpur Stairs', 204: '双层Purpur板Purpur Double Slab', 205: 'Purpur板Purpur Slab', 206: '末地石砖End Stone Bricks', 208: '草径Grass Path', 209: '末地门End Gateway', 210: '重复命令块Repeating Command Block', 211: '命令链块Chain Command Block', 255: '结构块Structure Block'}
