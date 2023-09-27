import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.integrate import odeint

g = 9.81 #m/s^2
l0 = 1 #m
k = 1 #N/m
m = 0.25 #kg
b = 0.2
time_interval = 45 #seconds
frms = time_interval*60 #frames

#defining integration function 
def integration(variables,t):
    (r, theta, rdot, omega) = variables
    sol_r = rdot # We can get the solution for r by integrating rdot
    sol_rdot = (l0+r)*(omega**2) - (k/m)*r + g*np.cos(theta)-(b*rdot) # We can get the solution for radial velocity(rdot) by integrating right side 
    #which we get by solving euler-lagrange equations for r 
    sol_theta = omega #integrating omega would give us theta
    sol_omega = -(((2*rdot*omega)+(g*np.sin(theta)))/(l0+r))-(b*omega) #integrating right side would give us omega according to euler lagrange equations for theta
    return [sol_r,sol_theta,sol_rdot,sol_omega]

#Initializing variables

r_0 = 0
rdot_0 = 0
theta_0 = 4*(np.pi/12)
omega_0 = 0

initial_variables = (r_0,theta_0,rdot_0,omega_0)

t = np.linspace(0,time_interval,frms) #creating a time list for oneint

solution = odeint(integration,y0=initial_variables,t=t) #getting solutions with odeint

#Defining solutions
r = solution[:,0] + l0 
theta = solution[:,1]
#Converting to carteesian coordinates
y = -r*np.cos(theta)
x = r*np.sin(theta)

#Plotting
fig,ax = plt.subplots()

timer = fig.text(0,0,str(0),size=10) #Addig timer

line1, = ax.plot([],[],'go:')
line2, = ax.plot([],[],color='gray')

#Scaling our plot
plt.xlim(-l0,l0)
plt.ylim((min(y)-1,0))
plt.xticks([]) #Deleting x scale

#Uptading values 
def animate1(i):
    line1.set_data([0,x[i]],[0,y[i]])
    line2.set_data(x[:i],y[:i])
    timer.set_text("Time = %.2f"%(i/60))

# ffmpeg is required to save the animation. You can download it from https://ffmpeg.org/ 
plt.rcParams['animation.ffmpeg_path'] = "C:\\Users\\furka\Downloads\\ffmpeg-6.0-essentials_build\\ffmpeg-6.0-essentials_build\\bin\\ffmpeg.exe"
# linking ffmpeg path for matplotlib.animation. Be careful with double slashes.
anim = animation.FuncAnimation(fig,animate1,frames=frms,interval=16.667) #Creating animation
anim.save('damped_elastic_pendulum_snake.mp4',dpi=150,fps=60,writer='ffmpeg')#Saving animation
