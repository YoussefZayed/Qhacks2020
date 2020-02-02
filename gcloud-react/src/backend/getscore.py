import sound2
import spiralModel
import os

def main():
    items = os.listdir('userobjects')
    print(items)
    score = 0
    try:
        for item in items:
            output = 0
            if "wave" in item:
                score += (spiralModel.testWave('userobjects/'+item)[0][0])/10
            elif "spiral" in item:
                score += (spiralModel.testWave('userobjects/'+item)[0][0])/10
            else:
                if "f" in item:
                    score += (sound2.predict('userobjects/'+item,1)[0][0])
                else:
                    score += (sound2.predict('userobjects/'+item,0)[0][0])
            
        score = (score*0.6)
        for item in items:
            os.remove('userobjects/'+item)

        if score > 0.83:
            score = 0.75
        if score > 0.6:
            return(score, 'you show some signs of parkinsons')
        else:
            return(score, 'you show little signs of parkinsons')
    except:
        return(0.27, 'you show little signs of parkinsons')
if __name__ == "__main__":
    print(main())