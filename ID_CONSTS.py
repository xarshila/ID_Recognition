ID_FRONT_CONSTS = {
    "photo" :   { 
        "y1":248, "y2": 660, "x1": 55, "x2": 400,
        "do_not_read": True
    },
    "name_ge" : {
        "y1":248, "y2": 295, "x1": 440, "x2": 920, 
        "lang" : "kat",
        "threshold": 0.85, 
        "v_crop_start":20, "v_crop_end": 80
    },
    "name_en" : {
        "y1":293, "y2": 347, "x1": 440, "x2": 920, 
        "lang": "eng",
        "threshold": 0.84, 
        "v_crop_start":20, "v_crop_end": 80,
        "config": "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8"
    },
    "last_name_ge" : {
        "y1":377, "y2": 420, "x1": 445, "x2": 920,
        "lang" : "kat",
        "threshold": 0.86, "v_crop_start":40, "v_crop_end": 80,
        "config": "-c tessedit_char_whitelist=აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ --psm 6"
    },
    "last_name_en" : {
        "y1":417, "y2": 472, "x1": 440, "x2": 920,
        "lang": "eng",
        "threshold": 0.788, "v_crop_start":20, "v_crop_end": 120,
        "config": "  tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8"
    },
    "card_id" :   {
        "y1":700, "y2": 755, "x1": 118, "x2": 400, 
        "lang" : "eng",
        "threshold": 0.77, "v_crop_start":10, "v_crop_end": 250,
        "config": " -c   tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789   --psm 8  "
    },
    "person_id" : {
        "y1":505,  "y2" : 560, "x1" : 800,  "x2" : 1040, 
        "lang" : "eng",
        "threshold": 0.64, "v_crop_start":10, "v_crop_end": 250,
        "config": "-c tessedit_char_whitelist=0123456789 tessedit_page_number=1 --psm 8 "
    },
    "nation":{
        "y1":505,  "y2" : 560, "x1" : 435,  "x2" : 540, 
        "lang" : "eng",
        "threshold": 0.8, "v_crop_start":10, "v_crop_end": 40,
        "config": "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8" 
    },
    "sex":{
        "y1":505,  "y2" : 560, "x1" : 695,  "x2" : 750, 
        "lang" : "eng",
        "threshold": 0.8, "v_crop_start":10, "v_crop_end": 40,
        "config": "-c tessedit_char_whitelist=MF --psm 8" 
    },
    "birth_date":{
        "y1":615,  "y2" : 670, "x1" : 435,  "x2" : 630, 
        "lang" : "eng",
        "threshold": 0.84, "v_crop_start":25, "v_crop_end": 180,
        "config": "-c tessedit_char_whitelist=1234567890. --psm 8" 
    },
    "exp_date":{
        "y1":615,  "y2" : 670, "x1" : 720,  "x2" : 920, 
        "lang" : "eng",
        "threshold": 0.84, "v_crop_start":25, "v_crop_end": 180,
        "config": "-c tessedit_char_whitelist=1234567890. --psm 8"  
    },
}
