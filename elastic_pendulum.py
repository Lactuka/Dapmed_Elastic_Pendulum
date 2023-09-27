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
frms = time_interval*60

def integration(variables,t):
    (r, theta, rdot, omega) = variables
    sol_r = rdot
    sol_rdot = (l0+r)*(omega**2) - (k/m)*r + g*np.cos(theta)-(b*rdot)
    sol_theta = omega
    sol_omega = -(((2*rdot*omega)+(g*np.sin(theta)))/(l0+r))-(b*omega)
    return [sol_r,sol_theta,sol_rdot,sol_omega]

r_0 = 0
rdot_0 = 0
theta_0 = 4*(np.pi/12)
omega_0 = 0

initial_variables = (r_0,theta_0,rdot_0,omega_0)

t = np.linspace(0,time_interval,frms)

solution = odeint(integration,y0=initial_variables,t=t)

r = solution[:,0] + l0
theta = solution[:,1]
y = -r*np.cos(theta)
x = r*np.sin(theta)

fig = plt.figure()
axes = plt.axes(xlim=(-1,1),ylim=(min(y)-1,0))

line1, = axes.plot([],[],'go:')
line2, = axes.plot([],[],color='gray')

def animate1(i):
    line1.set_data([0,x[i]],[0,y[i]])
    line2.set_data(x[:i],y[:i])

plt.rcParams['animation.ffmpeg_path'] = "C:\\Users\\furka\Downloads\\ffmpeg-6.0-essentials_build\\ffmpeg-6.0-essentials_build\\bin\\ffmpeg.exe"
anim = animation.FuncAnimation(fig,animate1,frames=frms,interval=16.667)
anim.save('damped_elastic_pendulum_snake.mp4',dpi=150,fps=60,writer='ffmpeg')