# importing the required module 
import matplotlib.pyplot as plt 

results = {'TSLA': 312, 'ICLN': 108, 'GOOD': 6, 'THCB': 14, 'LAZR': 13, 'PLUG': 28, 'FEYE': 33, 'SRAC': 9, 'EVER': 10, 'ENPH': 8, 'UK': 16, 'GOEV': 89, 'AAPL': 120, 'MVIS': 32, 'FCEL': 101, 'ZM': 15, 'TRIT': 3, 'BTWN': 20, 'MARA': 11, 'HUGE': 4, 'GRWG': 6, 'ABCL': 1, 'OSTK': 2, 'IBKR': 2, 'AMD': 81, 'HEAR': 3, 'ON': 33, 'GP': 1, 'PT': 23, 'CRSR': 80, 'PS': 2, 'MGNI': 17, 'GO': 38, 'NKLA': 41, 'DADA': 2, 'NVDA': 29, 'MAR': 1, 'BBBY': 3, 'RIOT': 18, 'RIDE': 5, 'INSG': 2, 'LI': 3, 'OPEN': 24, 'JD': 45, 'Z': 6, 'MSFT': 26, 'INO': 3, 'QQQJ': 8, 'ADP': 1, 'MRNA': 10, 'MCFE': 3, 'NEXT': 13, 'PHAR': 1, 'MDLZ': 1, 'RUN': 4, 'WATT': 1, 'INTC': 2, 'CDC': 1, 'HAS': 8, 'FVAM': 1, 'BIDU': 8, 'IQ': 7, 'CAN': 9, 'PDD': 21, 'AMZN': 64, 'DKNG': 28, 'TH': 3, 'JACK': 9, 'FREE': 3, 'THBR': 9, 'SRNE': 12, 'FB': 21, 'GOOG': 5, 'SYNC': 1, 'BRPA': 1, 'LIVE': 1, 'FLIR': 4, 'DBX': 1, 'GH': 7, 'SG': 1, 'LOOP': 1, 'OZON': 1, 'CRWD': 9, 'PTON': 18, 'SFIX': 2, 'PRCH': 2, 'ETSY': 3, 'EBON': 1, 'SSPK': 10, 'NICE': 2, 'STAY': 2, 'VERY': 3, 'ATVI': 3, 'BYND': 4, 'ZS': 3, 'ENG': 3, 'ROKU': 7, 'AAL': 4, 'EDIT': 4, 'QQQ': 16, 'JAN': 6, 'VLDR': 22, 'LOVE': 4, 'CHEF': 1, 'DARE': 1, 'BLNK': 56, 'VIAC': 1, 'TURN': 4, 'TLRY': 3, 'SP': 3, 'BNTX': 1, 'PACB': 
6, 'COKE': 2, 'FROG': 3, 'WKHS': 4, 'SMH': 2, 'GAN': 1, 'CFII': 1, 'ALOT': 3, 'CARE': 2, 'COST': 2, 'WOOD': 1, 'NBAC': 2, 'OLD': 1, 'PERI': 3, 'APHA': 5, 'TA': 15, 'PRPL': 19, 'LULU': 8, 'SATS': 4, 'VSAT': 4, 'SOLO': 5, 'TECH': 2, 'SPWR': 4, 'EXPI': 2, 'CRSP': 9, 'BOOM': 
2, 'HRTX': 1, 'CGC': 1, 'PLAY': 3, 'MASS': 2, 'TQQQ': 2, 'BIGC': 1, 'LCY': 1, 'WYNN': 1, 'NIU': 2, 'AUPH': 1, 'MU': 7, 'SURF': 1, 'IGAC': 1, 'NFLX': 2, 'FUTU': 1, 'MDB': 1, 'ABNB': 8, 'WISH': 8, 'AIRT': 2, 'GRVY': 2, 'HOPE': 1, 'FOX': 1, 'RING': 1, 'UAL': 2, 'ARKO': 1, 'FANG': 2, 'AFRM': 1, 'UPST': 3, 'BBQ': 1, 'CIIC': 4, 'ROOT': 2, 'LFTR': 1, 'FTC': 1, 'EYES': 1, 'FRHC': 2, 'UPWK': 3, 'CGRO': 3, 'AAWW': 
1, 'AAXN': 1, 'REAL': 3, 'EBAY': 1, 'SRACW': 2, 'TELL': 2, 'SBUX': 3, 'ULTA': 2, 'CYRX': 1, 'BL': 1, 'LRCX': 1, 'WNW': 1, 'VS': 1, 'UHAL': 1, 'REGI': 1, 'LIFE': 2, 'AZN': 2, 'SQQQ': 2, 'GOOGL': 3, 'HIMX': 2, 'FAT': 4, 'CD': 1, 'RAIL': 1, 'QELL': 3, 'VPN': 3, 'MTCH': 3, 'PYPL': 1, 'FORTY': 1, 'PI': 1, 'SUMO': 4, 'SFM': 1, 'MCHI': 1, 'AVGO': 1, 'VSPR': 2, 'GAIN': 3, 'DDOG': 2, 'CSIQ': 1, 'SGMO': 3, 'CAR': 1, 'GENE': 1, 'EA': 1, 'OKTA': 1, 'RAVN': 1, 'XP': 2, 'RDFN': 4, 'FAST': 1, 'FIVE': 1, 'CLOU': 1, 'CAMP': 1, 'PLUS': 1, 'GPRO': 1, 'ATNX': 1, 'BTBT': 1, 'ARCT': 1, 'GEVO': 1, 'BREZW': 1, 'CODA': 1, 'IPA': 1}

# x-coordinates of left sides of bars  
left = list(range(1,len(results)+1))
  
# heights of bars 
height = list(results.values())
  
# labels for bars 
tick_label = list(results.keys())
  
# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.4, color = ['red', 'green']) 
  
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
  
# function to show the plot 
plt.show() 