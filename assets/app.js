import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'
import RenderallpostsController from '../blog/javascript/controllers/renderallposts_controller'
import RendersinglepostController from'../blog/javascript/controllers/rendersinglepost_controller'

import "./app.css";
import "./bootstrap.min.css";


const application = Application.start()
const consumer = new WebsocketConsumer(`ws://${window.location.host}/ws/sockpuppet-sync`)

application.register("rendersinglepost", RendersinglepostController)
application.register("renderallposts", RenderallpostsController)
StimulusReflex.initialize(application, { consumer })


console.log("hello, world!");
console.log("good good good");
//document.getElementById("goodid").innerHTML = "Hello from Webpack! I'm refreshing automatically!";

