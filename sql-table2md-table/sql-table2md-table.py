if __name__=='__main__':
    import pyperclip
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, required=True, help='Specify the path to your INPUT file.', dest='file')
    pargs = parser.parse_args()
    
    class table2table:
        
        def __init__(self,INPUT):
            self.Ipath=INPUT
        
        def convertir(self):
            try:
                I=open(self.Ipath,'r', encoding='utf-8')
                lines=I.readlines()
                I.close()
                heading=lines[0]
                body=lines[1:]
                heading_blocks=(heading.replace('\n', '')).split('\t')
                print(f'\n\nSe creará una tabla con {len(heading_blocks)} columnas y {len(body)} filas\n')
                columnas=[]
                for x in body:
                    columnas.append((x.replace('\n','')).split('\t'))
                texto=''
                for x in heading_blocks:
                    if heading_blocks.index(x)==0:
                        texto+=f'|{x}|'
                    elif heading_blocks.index(x)==heading_blocks.index(heading_blocks[-1]):
                        texto+=f'{x}|\n'
                    else:
                        texto+=f'{x}|'

                for x in heading_blocks:
                    if heading_blocks.index(x)==0:
                        texto+=f'|---|'
                    elif heading_blocks.index(x)==heading_blocks.index(heading_blocks[-1]):
                        texto+=f'---|\n'
                    else:
                        texto+=f'---|'
                for x in columnas:
                    for y in x:
                        if x.index(y)==0:
                            texto+=f'|{y}|'
                        elif x.index(y)==x.index(x[-1]):
                            texto+=f'{y}|\n'
                        else:
                            texto+=f'{y}|'
                pyperclip.copy(texto)

                print(texto)
            except:
                print('Error: Something went wrong. Try again and remember to specify the path to your input file correctly :) .')

sql2md=table2table(pargs.file)
if pargs.file:
    sql2md.convertir()
