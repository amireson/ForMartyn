# Heat transport in a saturated, hydrostatic soil

Andrew, Ines and Seth

Consider a control volume of soil, where

$$V=\Delta x\Delta y \Delta z$$

$$V=V_I+V_L+V_S+V_G$$

$$M=M_I+M_L+M_S+M_G$$

where $V$ is volume and $M$ is mass, and subscripts are for the different components, specifically liquid, $L$, ice, $I$, soil solid matter, $S$, and gas, $G$. The density of a component, $\rho_i$ is

$$\rho_i=\frac{M_i}{V_i}$$

### Volume fractions

Let $\theta_i$ represent the volume of a given component $i$ (where ice, liquid, etc, are the components) per volume, so

$$\theta_i=\frac{V_i}{V}$$


### Mass fractions

Let $m_i$ represent the mass of a given component, $i$, per volume. Then

$$m_i=\frac{M_i}{V}=\rho_i\theta_i$$

### Mass balance

We assume we are dealing with a closed system with respect to water - so there is no inflow or outflow. The continuity equation is:

$$\Delta M = 0$$

Therefore we have

$$\Delta(M_I+M_L+M_S+M_G)=0$$

We know that $M_S$ is constant, hence $\Delta M_S=0$. We assume that $M_G\approx0$, so $\Delta M_G=0$. Therefore

$$\Delta(M_I+M_L)=0$$

On a per unit volume basis we have

$$\Delta(m_I+m_L)=\Delta(\rho_I\theta_I+\rho_L\theta_L)=0$$

Since we are talking about changes in time, we can write

$$\frac{d}{dt}(\rho_I\theta_I+\rho_L\theta_L)=0$$

and since the densities are constant,

$$\rho_I\frac{d\theta_I}{dt}=-\rho_L\frac{d\theta_L}{dt}$$

and

$$\frac{d\theta_L}{dt}=-\frac{\rho_I}{\rho_L}\frac{d\theta_I}{dt}$$

This is the mass balance equation for the situation where the water doesn't move.




### Energy balance

Let $U$ (J) be the internal energy of the control volume, and $u$ (J/m$^3$) be the internal energy per unit volume. The change in internal energy is due to the exchange of energy (heat) with the surroundings. The incoming heat flux in the vertical direction is $H_{in}$ and the outgoing heat flux in the vertical direction is $H_{out}=H_{in}+\Delta H$, (both in J/m$^2$/s). Then

$$\Delta U =V\Delta u= -\Delta H\Delta x \Delta y \Delta t$$

and

$$\frac{\Delta u}{\Delta t} = \frac{\Delta H}{\Delta z}$$

or

$$\frac{\partial u}{\partial t}=-\frac{\partial H}{\partial z}$$

We now have to deal with the left hand side, that is the changes in internal energy, and the right hand side, that is the net addition, or removal, of heat. These can be treated separately. 

### Net exchange of heat

Since we are neglecting the movement of water, we can ignore advection and have heat transport only by diffusion. Diffusive transport is described by Fick's first law

$$H=-D\frac{dT}{dz}$$

And the right hand side of the continuity equation is simply Fick's second law, which is

$$\frac{\partial u}{\partial t}=D\frac{\partial^2 T}{\partial z^2}$$

### Changes in internal energy for a single component

The internal energy takes an arbitrary value - we are only interested in relative changes in energy. Changes in energy are due to sensible and latent heat. Internal energy associated with sensible heat, $U_{SEN}$ (J) or $u_{SEN}$ (J/m$^3$), is the energy stored in a material as a function of it's temperature, such that

$$\Delta U_{SEN,i}=\Delta (C_iM_iT_i)$$

or 

$$\Delta u_{SEN,i}=\Delta(C_im_iT_i)$$

or 

$$\Delta u_{SEN,i}=\Delta(C_i\theta_i\rho_i T_i)$$

where $C$ is the specific heat capacity (J/kg/K - i.e. the energy per mass per degree). Note that the specific heat can, in general, change due to a change in temperature, $T$, or due to a change in amount of a component, $m$, or both.

Internal energy associated with latent heat, $U_{LAT}$ (J) or $u_{LAT}$ (J/m$^3$), is the energy stored in a material as a function of the structure of the molecules, with solids having less internal energy than liquids and liquids having less internal energy than gases. Changes in internal energy associated with latent heat occur when a material changes phase, and is given by

$$\Delta U_{LAT}=\Delta(\lambda M)$$

or 

$$\Delta u_{LAT}=\Delta(\lambda m)$$

### Changes in interal energy in the soil control volume

Since the soil has four components, and three of these are dynamic, the change in internal energy can be written:

$$\Delta u=\Delta u_I+\Delta u_L+\Delta u_S+\Delta u_G$$

and further, the internal energy of a single component, $i$, is given by

$$\Delta u_i=\Delta u_{SEN,i}+\Delta u_{LAT,i}$$

meaning we end up with the following eight terms:

$$\begin{array}{ll}
\Delta u= & \Delta(C_Im_IT_I)+\Delta(C_Lm_LT_L)+\Delta(C_Sm_ST_S)+\Delta(C_Gm_GT_G)\\
 & +\Delta(\lambda_I m_I)+\Delta(\lambda_L m_L)+\Delta(\lambda_S m_S)+\Delta(\lambda_G m_G)
\end{array}$$

Now, since we have no phase change associated with the soil solids or the gas (in this case), we can ignore the last two terms. We can also make the important assumption that the components of our soil are all in thermal equilibrium, hence

$$T=T_I=T_L=T_S=T_G$$

So, considering changes with time we can write

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=&\displaystyle C_I\frac{d(m_IT)}{dt}+C_L\frac{d(m_LT)}{dt}+C_S\frac{d(m_ST)}{dt}+C_G\frac{d(m_GT)}{dt}\\
 &\displaystyle +  \lambda_I\frac{dm_I}{dt}+\lambda_L\frac{dm_L}{dt}
 \end{array}
$$

and

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=&\displaystyle \frac{dT}{dt}\left(C_Im_I+C_Lm_L+C_Sm_S+C_Gm_G\right)\\
 &\displaystyle + C_IT\frac{dm_I}{dt}+C_LT\frac{dm_L}{dt}+C_ST\frac{dm_S}{dt}+C_GT\frac{dm_G}{dt}\\
 &\displaystyle +  \lambda_I\frac{dm_I}{dt}+\lambda_L\frac{dm_L}{dt}
 \end{array}
$$

Since there is no change in mass of soil solids, and the change in air mass is negligible, we have

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=& \displaystyle \frac{dT}{dt}\left(C_Im_I+C_Lm_L+C_Sm_S+C_Gm_G\right)\\
 &\displaystyle + (C_IT+\lambda_I)\frac{dm_I}{dt}+(C_LT+\lambda_L)\frac{dm_L}{dt}
 \end{array}
$$

or

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=& \displaystyle \frac{dT}{dt}\left(C_I\theta_I\rho_I+C_L\theta_L\rho_L+C_S\theta_S\rho_S+C_G\theta_G\rho_G\right)\\
 &\displaystyle + (C_IT+\lambda_I)\rho_I\frac{d\theta_I}{dt}+(C_LT+\lambda_L)\rho_L\frac{d\theta_L}{dt}
 \end{array}
$$

(Note, do the last two terms above explain why the apparent latent heat capacity is a function of temperature? Maybe.)

At this point, if we examine the equation above, we are left with the question, how can we know how a certain amount of net energy exchange (i.e. from the diffusion equation above) is partitioned between changes in sensible and latent heat. I'm not sure that there is a completely rigorous solution beyond this point for the general case. However, we will now make a simplifying assumption - that is, assume that the soil is completely saturated.



### Changes in internal energy in a saturated soil

The change in internal energy for a saturated (with liquid or ice) soil is now given by

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=& \displaystyle \frac{dT}{dt}\left(C_I\theta_I\rho_I+C_L\theta_L\rho_L+C_S\theta_S\rho_S\right)\\
 &\displaystyle + (C_IT+\lambda_I)\rho_I\frac{d\theta_I}{dt}+(C_LT+\lambda_L)\rho_L\frac{d\theta_L}{dt}
 \end{array}
$$

Recall from the water balance equation we have 

$$\frac{d\theta_I}{dt}=-\frac{\rho_L}{\rho_I}\frac{d\theta_L}{dt}$$

so

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=& \displaystyle \frac{dT}{dt}\left(C_I\theta_I\rho_I+C_L\theta_L\rho_L+C_S\theta_S\rho_S\right)\\
 &\displaystyle - (C_IT+\lambda_I)\rho_L\frac{d\theta_L}{dt}+(C_LT+\lambda_L)\rho_L\frac{d\theta_L}{dt}
 \end{array}
$$

and

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=& \displaystyle \frac{dT}{dt}\left(C_I\theta_I\rho_I+C_L\theta_L\rho_L+C_S\theta_S\rho_S\right)\\
 &\displaystyle \frac{d\theta_L}{dt}\left(T\rho_L(C_L-C_I)+\rho_L(\lambda_L-\lambda_I)\right)
 \end{array}
$$

Now, we also know that due to freezing point depression, we have a relationship between the liquid water content, $\theta_L$ and the temperature. Lets assume that this is

$$\theta_L=f(T)$$

Hence

$$\frac{d\theta_L}{dT}=f'(T)$$

where $f(T)$ and $f'(T)$ are parametric expressions. Now we can write

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=& \displaystyle \frac{dT}{dt}\left(C_I\theta_I\rho_I+C_L\theta_L\rho_L+C_S\theta_S\rho_S\right)\\
 &\displaystyle \frac{dT}{dt}f'(T)\left(T\rho_L(C_L-C_I)+\rho_L(\lambda_L-\lambda_I)\right)
 \end{array}
$$

Or in otherwords:

$$\begin{array}{ll}
\displaystyle
\frac{du}{dt}=& \displaystyle \frac{dT}{dt}\left(C_I\theta_I\rho_I+C_L\theta_L\rho_L+C_S\theta_S\rho_S + f'(T)\left(T\rho_L(C_L-C_I)+\rho_L(\lambda_L-\lambda_I)\right)\right)
 \end{array}
$$

### Governing equation for heat transport in a saturated frozen soil with no movement of water

$$\frac{\partial T}{\partial t}\left(C_I\theta_I\rho_I+C_L\theta_L\rho_L+C_S\theta_S\rho_S + f'(T)\left(T\rho_L(C_L-C_I)+\rho_L(\lambda_L-\lambda_I)\right)\right)=D\frac{\partial^2 T}{\partial z^2}$$

Note, for $T$ values not close to zero degrees celcius, $f'(T)$ is zero, and hence there are no latent heat effects. 

Also note, we have not here defined how $D$ is also a function of the different components, which is important, but simple to define.

# The VG equations

van Genuchten:

$$\frac{\theta-\theta_R}{\theta_S-\theta_R}=S_e=(1+(\alpha\psi)^n)^{-m}$$

$$\theta=\theta_R+(\theta_S-\theta_R)(1+(\alpha\psi)^n)^{-m}$$

It can be shown (ask me for my derivation) that the slope of this is given by

$$\frac{d\theta}{d\psi}=\frac{-(\theta_S-\theta_R)m\alpha}{1-m}S_e^{1/m}(1-S_e^{1/m})^m$$

### The GCE Equation

Start from this

$$dG_I=-S_IdT+\nu_IdP_I=dG_L=-S_LdT+\nu_LdP_L$$

where $S$ is the entropy per mass, and $\nu$ is the specific volume, which is $1/\rho$. Assume $dP_I=0$ and $S_L-S_I=L_f/T$, then

$$\frac{L_f}{T}dT=\nu_LdP_L$$

Therefore

$$P-P_0=\frac{L_f}{T_0\nu}(T-T_0)$$

and

$$\psi=\frac{L_f}{gT_0}T$$

where $T$ is in degrees C, and $T_0$ is 273.15 K.

### The SFC and CFC curves

Substituting the above into the van Genuchten model we get the SFC

$$S_e=\left(1+\left(\alpha\frac{L_f}{gT_0}T\right)^n\right)^{-m}$$

$$\theta_L=\theta_R+(\theta_S-\theta_R)S_e$$

and the CFC (which is the slope of the SFC)

$$\frac{d\theta_L}{dT}=\frac{-(\theta_S-\theta_R)m\alpha\frac{L_f}{gT_0}}{1-m}S_e^{1/m}(1-S_e^{1/m})^m$$

Which is

$$\frac{d\theta_L}{dT}=\frac{d\theta_L}{d\psi}\frac{L_f}{gT_0}$$


