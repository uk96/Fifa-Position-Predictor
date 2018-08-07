from flask import flash
import csv

class Printer(object):
	def show_string(self,d,f,spo,sp,v,lp,i,st,slt,gkd,gkr,gkp,forw,mid,defn,goal,sum1):
		n=10000
		ch=[d,f,spo,sp,v,lp,i,st,slt,gkd,gkr,gkp]
		fprob = 1
		mprob = 1
		dprob = 1
		gprob = 1
		if d=='':
			flash("You didn't enter any text to flash")
		else:
			fprob=(1.0*forw[0][d]*forw[1][f]*forw[2][spo]*forw[3][sp]*forw[4][v]*forw[5][lp]*forw[6][i]*forw[7][st]*forw[8][slt]*forw[9][gkd]*forw[10][gkr]*forw[11][gkp])/(1.0*sum1[0]**11)
			mprob=(1.0*mid[0][d]*mid[1][f]*mid[2][spo]*mid[3][sp]*mid[4][v]*mid[5][lp]*mid[6][i]*mid[7][st]*mid[8][slt]*mid[9][gkd]*mid[10][gkr]*mid[11][gkp])/(1.0*sum1[1]**11)
			dprob=(1.0*defn[0][d]*defn[1][f]*defn[2][spo]*defn[3][sp]*defn[4][v]*defn[5][lp]*defn[6][i]*defn[7][st]*defn[8][slt]*defn[9][gkd]*defn[10][gkr]*defn[11][gkp])/(1.0*sum1[2]**11)
			gprob=(1.0*goal[0][d]*goal[1][f]*goal[2][spo]*goal[3][sp]*goal[4][v]*goal[5][lp]*goal[6][i]*goal[7][st]*goal[8][slt]*goal[9][gkd]*goal[10][gkr]*goal[11][gkp])/(1.0*sum1[3]**11)			
			flash("Predicted Positioning: "+str(spo))
			flash("Predicted Long Passing: "+str(lp))
			flash("Predicted SLiding Tackle: "+str(slt))
			flash("Predicted GK Positioning: "+str(gkp))
			#flash(sum[1])
			#flash(sum[2])
			#flash(sum[3])
			#flash(fprob)
			#flash(mprob)
			#flash(dprob)
			#flash(gprob)
			if fprob==0.0 and mprob==0.0 and dprob==0.0 and gprob==0.0:
				if spo>=lp and spo>=slt and spo>=gkp:
					flash("The Player is a Forward")
				elif lp>=slt and lp>=gkp and lp>=spo:
					flash("The Player is a Midfielder")
				elif slt>=lp and slt>=spo and slt>=gkp:
					flash("The Player is a Defender")
				else:
					flash("The Player is a GoalKeeper")
			elif fprob >= mprob and fprob >= dprob and fprob >=gprob:
				flash("The Player is a Forward")
			elif mprob >= dprob and mprob >= gprob and mprob>=fprob:
				flash("The Player is a Midfielder")
			elif dprob >= gprob and dprob>=mprob and dprob>=fprob:
				flash("The Player is a Defender")
			else:
				flash("The Player is a GoalKeeper")