import square_extract


album_success = 0
album_total = 0
print('=========================\nTESTING THE SQUARE API FETCHER\n=========================\n')
print('Testing Album Detection function\n')
print('Testing Unknown Album')
album_total += 1
if square_extract.get_artist('aaaaaaa') == 'Unknown':
    print('Success')
    album_success += 1
else:
    print('Fail')

print('Testing STRAY KIDS Album')
album_1 = square_extract.get_artist('Stray Kids - I am Not (Random Version)')
print(f'Correct Album: Stray Kids. Obtained Album: {album_1}')
album_total += 1
if album_1 == 'Stray Kids':
    print('Success')
    album_success += 1
else:
    print('Fail')

print('Testing Ateez Album')
album_total += 1
album_2 = square_extract.get_artist('Ateez The World EP.FIN : Will (Platform Ver.)')
print(f'Correct Album: ATEEZ. Obtained Album: {album_2}')
if album_2 == 'ATEEZ':
    print('Success')
    album_success += 1
else:
    print('Fail')

print('Testing Enhypen Album')
album_total += 1
album_3 = square_extract.get_artist('Enhypen-Romance : Untold')
print(f'Correct Album: ENHYPEN. Obtained Album: {album_3}')
if album_3 == 'ENHYPEN':
    print('Success')
    album_success += 1
else:
    print('Fail')


print('Testing BTS Album')
album_total += 1
album_4 = square_extract.get_artist('BTS Butter (Random Ver.)')
print(f'Correct Album: BTS. Obtained Album: {album_4}')
if album_4 == 'BTS':
    print('Success')
    album_success += 1
else:
    print('Fail')

print('Testing (G)I-DLE Album')
album_total += 1
album_5 = square_extract.get_artist('(G)I-DLE - 2 (Random Ver.)')
print(f'Correct Album: (G)I-DLE. Obtained Album: {album_5}')
if album_5 == '(G)I-DLE':
    print('Success')
    album_success += 1
else:
    print('Fail')

print(f'\nAPI Fetcher Result: {album_success}/{album_total}\n')
# ======================================================================================================
api_success = 0
api_total = 0
print('Testing API Fetcher for each order\n')



print('Testing Order #1')

try:
    api_total += 1
    order_1 = square_extract.fetch_order('wMWlo8dfGxQrxrVVSRnsOs4eV')
    print('Function Execution: Success')
    api_success += 1
except Exception as e:
    print(f'Function Execution Error: {e}')

api_total += 1
try:
    if len(order_1)==3:
        print('Correct number of items obtained(3): Success')
        api_success += 1
    else:
        print(f'Wrong number of items obtained:3 vs {len(order_1)}: Fail')
except Exception as e:
    print(f'Error occured during object count: {e}')

api_total += 1
try:
    print(f'Items are Supposed to be BTS Butter (Random Ver.), BTS Map of the Soul: Persona (Random Ver.), Paper Pag')
    print(f'Output from the call: {[item["name"] for item in order_1]}')
    if order_1[0]['name']=='BTS Butter (Random Ver.)' and order_1[1]['name']=='BTS Map of the Soul: Persona (Random Ver.)' and order_1[2]['name']=='Paper Bag':
        print('Correct Items obtained: Success')
        api_success += 1
    else:
        print('Fail')
except Exception as e:
    print(f'Error occurred during name check: {e}')

api_total += 1
try:
    print(f'Prices (c) supposed to be 3795, 3595, 100')
    print(f'Output from the call: {[item["total_money"]["amount"] for item in order_1]}')
    if order_1[0]['total_money']['amount']==3795 and order_1[1]['total_money']['amount']==3595 and order_1[2]['total_money']['amount']==100:
        print('Correct Prices obtained: Success')
        api_success += 1
    else:
        print('Fail')
    
except Exception as e:
    print(f'Error occurred during price check: {e}')



print('\nTesting Order #2')

try:
    api_total += 1
    order_1 = square_extract.fetch_order('gky9J28VhDV0CC6ZlDnnUc5eV')
    print('Function Execution: Success')
    api_success += 1
except Exception as e:
    print(f'Function Execution Error: {e}')

api_total += 1
try:
    if len(order_1)==1:
        print('Correct number of items obtained(3): Success')
        api_success += 1
    else:
        print(f'Wrong number of items obtained:1 vs {len(order_1)}: Fail')
except Exception as e:
    print(f'Error occured during object count: {e}')

api_total += 1
try:
    print(f'Items are Supposed to be Enhypen Orange Blood (Random Ver.)')
    print(f'Output from the call: {[item["name"] for item in order_1]}')
    if order_1[0]['name']=='Enhypen Orange Blood (Random Ver.)':
        print('Correct Items obtained: Success')
        api_success += 1
    else:
        print('Fail')
        
except Exception as e:
    print(f'Error occurred during name check: {e}')

api_total += 1
try:
    print(f'Prices (c) supposed to be 3995')
    print(f'Output from the call: {[item["total_money"]["amount"] for item in order_1]}')
    if order_1[0]['total_money']['amount']==3995:
        print('Correct Prices obtained: Success')
        api_success += 1
    else:
        print('Fail')
        
except Exception as e:
    print(f'Error occurred during price check: {e}')





print(f'\nAPI Fetcher Result: {api_success}/{api_total}\n')



