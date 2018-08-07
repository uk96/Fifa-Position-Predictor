from project import app
from project.models import Printer
from flask import render_template, request
import csv

@app.route('/')
def start():
    return render_template('print.html')

@app.route('/print',methods=['POST'])
def printer():
	if request.method=='POST':
		with open(r'C:\Users\Uddhesh Kadu\Desktop\Project\Fifa-Position-Predictor\project\fifa_players.csv',encoding="utf_8") as csvfile:
			reader = csv.DictReader(csvfile)
			table=[]
			i=0
			n=10000
			sum_value=[0,0,0,0]
			for row in reader:
				#print(i)
				if i==n:
					break
				i=i+1
				row1=[]
				row1.append(row['Dribbling'])
				row1.append(row['Finishing'])
				row1.append(row['Positioning'])
				row1.append(row['Vision'])
				row1.append(row['Short passing'])
				row1.append(row['Long passing'])
				row1.append(row['Marking'])
				row1.append(row['Standing tackle'])
				row1.append(row['Sliding tackle'])
				row1.append(row['GK reflexes'])
				row1.append(row['GK diving'])
				row1.append(row['GK positioning'])
				flag=0
				for val in row1:
					if len(val)>2 or len(val)==0:
						flag=1;
				if flag==1:
					continue
				pos=row['Preferred Positions'].split(' ');
				temp=[]
				for io in range(0,4,1):
					temp.append(0)
				forward=["ST","LW","RW","CF","LS","LF","RS","RF"]
				midfielder=["CM","CAM","CDM","LAM","LCM","LDM","CM","RAM","RCM","RDM","RM"]
				defender=["CB","LB","LCB","LWB","RB","RCB","RWB"]
				goalkeeper=["GK"]
				for val in pos:
					if val in forward:
						temp[0]=1
					elif val in midfielder:
						temp[1]=1
					elif val in defender:
						temp[2]=1
					elif val in goalkeeper:
						temp[3]=1
				row2=[]
				for value1 in row1:
					row2.append(value1)
				if temp[0]==1:
					row2.append("F")
					table.append(row2)
					sum_value[0]=sum_value[0]+1
				if temp[1]==1:
					row2.append("M")
					table.append(row2)
					sum_value[1] = sum_value[1] + 1
				if temp[2]==1:
					row2.append("D")
					table.append(row2)
					sum_value[2]=sum_value[2] + 1
				if temp[3]==1:
					row2.append("G")
					table.append(row2)
					sum_value[3]=sum_value[3] + 1
			for i in range(0,n,1):
				for j in range(0,12,1):
					table[i][j]=int(table[i][j])
			forward_table=[]
			for j in range(0,12,1):
				temporary=[]
				for y in range(0,100,1):
					temporary.append(0)
				for i in range(0,n,1):
					if table[i][12]=="F":
						temporary[table[i][j]]=temporary[table[i][j]]+1
				forward_table.append(temporary)
			#print(forward_table)
			mid_table=[]
			for j in range(0,12,1):
				temporary=[]
				for y in range(0,100,1):
					temporary.append(0)
				for i in range(0,n,1):
					if table[i][12]=="M":
						temporary[table[i][j]]=temporary[table[i][j]]+1
				mid_table.append(temporary)
			#print(mid_table)
			defender_table=[]
			for j in range(0,12,1):
				temporary=[]
				for y in range(0,100,1):
					temporary.append(0)
				for i in range(0,n,1):
					if table[i][12]=="D":
						temporary[table[i][j]]=temporary[table[i][j]]+1
				defender_table.append(temporary)
			#print(defender_table)
			goal_table=[]
			for j in range(0,12,1):
				temporary=[]
				for y in range(0,100,1):
					temporary.append(0)
				for i in range(0,n,1):
					if table[i][12]=="G":
						temporary[table[i][j]]=temporary[table[i][j]]+1
				goal_table.append(temporary)
			a = [0,0,0,0]
			b = [0,0,0,0]
			for j in range(0,4,1):	
				xsquare=0.0
				x=0.0
				xy=0.0
				y=0.0
				for i in range(0,n,1):
					y=y+table[i][j*3+2]
					x=x+table[i][j*3+1]
					xsquare=xsquare+(table[i][j*3+1]*table[i][j*3+1])
					xy=xy+(table[i][j*3+1]*table[i][j*3+2])
				a[j]=((y*xsquare)-(x*xy))/((n*xsquare)-(x*x))
				b[j]=((n*xy)-(x*y))/((n*xsquare)-(x*x))
				print (a[j])
				print (b[j])
			nik=int(request.form['finishing'])	
			spo=int(a[0]+(b[0])*(nik))
			print (spo)		
			lp=int(a[1]+(b[1])*(int(request.form['short_passing'])))
			print (lp)		
			slt=int(a[2]+(b[2])*(int(request.form['standing_tackle'])))
			print (slt)		
			gkp=int(a[3]+(b[3])*(int(request.form['gk_diving'])))
			print (gkp)
			printer = Printer()
			printer.show_string(int(request.form['dribbling']),int(request.form['finishing']),spo,int(request.form['vision']),int(request.form['short_passing']),lp,int(request.form['marking']),int(request.form['standing_tackle']),slt,int(request.form['gk_reflexes']),int(request.form['gk_diving']),gkp,forward_table,mid_table,defender_table,goal_table,sum_value)
		return render_template('layout.html')
	return render_template('print.html')


