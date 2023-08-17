def ptg(pt):
    pt = int(pt)
    pt_dictionary = {
        103: 1, 104: 1, 111: 1, 118: 1, 160: 1,
        998: 1, 

        106: 2, 112: 2,

        113: 3, 114: 3, 115: 3, 116: 3, 120: 3, 
        142: 3, 150: 3, 199: 3, 997: 3, 503: 3, 
        504: 3, 510: 3, 511: 3, 699: 3, 700: 3, 
        701: 3, 711: 3, 713: 3,

        119: 9, 

        506: 10, 509: 10, 566: 10, 660: 10, 760: 10,
        916: 10, 
        
        524: 11, 540: 11, 547: 11, 560: 11, 576: 11, 
        
        500: 20, 513: 20, 514: 20, 515: 20, 516: 20, 
        517: 20, 518: 20, 523: 20, 525: 20, 527: 20, 
        529: 20, 536: 20, 537: 20, 539: 20, 548: 20, 
        549: 20, 553: 20, 574: 20, 575: 20, 559: 20, 
        561: 20, 562: 20, 571: 20, 573: 20, 581: 20, 
        582: 20, 583: 20, 584: 20, 585: 20, 591: 20, 
        596: 20, 649: 20, 775: 20, 528: 20, 675: 20,
        
        200: 30, 
        203: 30, 550: 30, 552: 30, 554: 30, 555: 30,
        695: 30, 795: 30, 811: 30, 816: 30, 850: 30,
        812: 30, 915: 30, 
        
        556: 31, 558: 31, 590: 31, 592: 31, 593: 31, 594: 31, 
        595: 31, 597: 31, 
        
        951: 40, 954:40, 953: 40, 

        956: 41, 
        
        117: 49, 278: 49, 567: 49, 577: 49, 901: 49, 
        902: 49, 905: 49, 911: 49, 913: 49, 920: 49, 
        921: 49, 922: 49,
        952: 49, 955: 49, 957: 49, 960: 49, 961: 49, 
        990: 49
        }
    try:
        return pt_dictionary[pt]
    except KeyError:
        return None

def invert_dict():
    sfh = [
        103, 104, 111, 118, 160, 998
        ]
    duplex = [
        106, 112
        ]
    mfh = [
        113, 114, 115, 116, 120, 142, 150, 199, 
        997, 503, 504, 510, 511, 699, 700, 701, 
        711, 713
        ]
    h_unkn = [
        119
        ]
    office = [
        506, 509, 566, 660, 760, 916
              ]
    med = [
        524, 540, 547, 560, 576
        ]
    retail = [
        500, 513, 514, 515, 516, 517, 518, 528, 
        523, 525, 527, 529, 536, 537, 539, 548, 
        549, 553, 574, 575, 559, 561, 562, 571, 
        573, 581, 582, 583, 584, 585, 591, 596, 
        649, 675, 775
        ]
    ind = [
        200, 203, 550, 552, 554, 555, 695, 795, 
        811, 812, 816, 850, 915
        ]
    ind_whs = [
        556, 558, 590, 592, 593, 594, 595, 597
        ]
    govt = [
        951, 953, 954
        ]
    church = [
        956
        ]
    oth_unk = [
        117, 278, 567, 577, 901, 902, 905, 911,
        913, 920, 921, 922,
        952, 955, 957, 960, 961, 990
        ]
    
    pt_dct = {
        1:sfh, 2:duplex, 3:mfh, 9: h_unkn,
        10:office, 11:med,
        20:retail,
        30:ind, 31:ind_whs,
        40:govt, 41:church, 49:oth_unk
        }
    
    pt_inv_dict = {}
    for k in pt_dct:
        for n in pt_dct[k]:
            pt_inv_dict[n] = k
    
    print(pt_inv_dict)

    
categories = ['102 Res-Appealed Value', '103 Res-Obsolesced Value', '104 Modular', '105 Fraternity / Sorority', '106 Res Mother-Law Apt', '110 Apt Conversion', '111 Single Family Res.', '112 Duplex', '113 3‑4 Unit Apt', '114 5‑9 Unit Apt', '115 10‑19 Unit Apt', '116 Condo Unit', '117 Improved Rec.', '118 Manuf. Home', '119 PUD', '120 20‑49 Unit Apt', '142 Low-Inc-Hous-TC', '150 50‑98 Unit Apt', '160 Trailer Park', '199 99+ Unit Apt', '200 Industrial / Other', '202 Ind. Conversion', '203 Industrial Mixed', '500 Commercial / Other', '501 Building Salvage', '503 Retail Mixed', '504 Apt Mixed', '505 Conversion Other', '506 Office Conversion', '507 Retail Conversion', '509 Office Mixed', '510 Comm Imps in Res Zone', '511 Res Impr On Comm', '512 Duplex On Comm', '513 Auto Service Center', '514 Auto Dealership', '515 Bank', '516 Used Car Lot', '517 Bowling Alley', '518 Car Wash', '520 Comm EV', '521 Res EV', '523 Convenience Store', '524 Nursing Hospital', '525 Drug Store', '527 Day Care Center', '528 Department Store', '529 Discount Store', '530 Laundromat', '535 Fraternal Building', '536 Mini Lube', '537 Service Garage', '538 Storage Garage', '539 Lounge', '540 Group Care Home', '541 Hangar - Exempt', '542 Airport Hangar', '543 Airport - Exempt', '544 Exempt Hangar-Vac', '545 Exempt Concessnaire', '547 Hospital', '548 Hotel - Limited', '549 Hotel', '550 Ind - Light - Mfg', '551 Auto Showroom', '552 Ind - RE', '553 Health Club', '554 Ind Heavy Mfg', '555 Ind Light Shell', '556 Cold Storage', '557 Loft', '558 Flex', '559 Market', '560 Medical Office', '561 Mortuary', '562 Motel', '563 Apt High Rise', '564 Bed and Breakfast', '566 Office', '567 Parking Structure', '570 Post Office', '571 Reception Center', '573 Restaurant', '574 Fast Food Restaurant', '575 Retail Store', '576 Retirement Home', '577 School Private', '578 Service Station', '581 Neighborhood Ctr', '582 Community Mall', '583 Regional Mall', '584 Retail Service', '585 Strip Center', '590 Office / Warehouse', '591 Theater', '592 Distribution Whse', '593 Mini Warehouse', '594 Storage Warehouse', '595 Transit Warehouse', '596 Discount Warehouse', '611 Condo Timeshare', '612 Condo MC Timeshar', '613 Condo 3‑4 Unit Apt', '614 Condo 5‑9 Unit Apt', '615 Condo10‑19 Unit Apt', '620 Condo20-49 Unit Apt', '649 Condo Hotel', '650 Condo 50‑98 Unit Apt', '660 Condo Office', '675 Condo Retail', '695 Condo Industrial', '699 Condo 99+ Unit Apt', '700 Common Area', '701 Common Area PUD', '711 Condo Comm Master', '713 Apt Common Master', '749 Hotel Comm Master', '760 Office Comm Master', '775 Retail Comm Master', '795 Ind Common Master', '811 Agri- Farm Animals', '812 Agri- Prod Grain', '816 Agri Livestock Ranch', '817 Agriculture Poultry', '818 Dairy', '830 Forest', '850 Mining', '888 Res - No Res Exempt', '889 Condo-No Res Exempt', '901 Vacant Lot - Res', '902 Vacant Lot - Ind', '903 Vacant Lot - MH', '904 Comm-Parkg Lot', '905 Vacant Land - Comm', '906 Comm Condo Vac Land', '907 Res Condo Parkg Stal', '908 Res Condo Vac Lot', '909 Res Condo Storg Lock', '910 Res Condo RV Parkg', '911 Vac Residential Lot', '912 Vac Assoc-Comm/Ind', '913 Vacant Assoc - MH', '914 Associated Retail', '915 Associated Industrial', '916 Associated Office', '917 Vacant Assoc - Rec', '918 Mobile Home Lot Vac', '922 PUD Lot', '927 Comm Condo Park Stal', '929 Comm Condo Storg Unt', '950 Irrigation', '951 Public', '953 Gov Bldg / Land', '954 School', '955 Other Exempt', '956 Church', '957 Related Parcel', '958 Com Irrigation', '960 Golf Course', '961 Cemetery', '971 Residential Imp BoE', '972 Duplex BoE', '976 Condo BoE', '977 Recreational BoE', '978 Mobile Home BoE', '979 PUD BoE', '990 Other Improvements', '993 Residential-Salvage', '994 Mobile Home - RP', '995 Mobile Home - PP', '996 Condo- Model', '997 Residential - Multi', '998 SF Res- Model', '999 Undevelopable']

def return_provided_class_descriptions(classes):
    for typ in categories:
        prt = typ.partition(' ')
        if int(prt[0]) in classes:
            print('   * `' + prt[0] + '` ' + prt[2])