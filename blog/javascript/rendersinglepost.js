import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'
import RendersinglepostController from './controllers/rendersinglepost_controller'

const application = Application.start()
const consumer = new WebsocketConsumer(`ws://${window.location.host}/ws/sockpuppet-sync`)

application.register("rendersinglepost", RendersinglepostController)
StimulusReflex.initialize(application, { consumer })
