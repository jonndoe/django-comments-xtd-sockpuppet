import { Controller } from 'stimulus';
import StimulusReflex from 'stimulus_reflex';

export default class extends Controller {
  connect() {
    StimulusReflex.register(this)
  }

  increment(event) {
    console.log('increment')
    event.preventDefault()
    this.stimulate('rendersinglepostReflex#increment', 1)
  }

  render(event) {
    console.log('render_single_post')
    event.preventDefault()
    this.stimulate('rendersinglepostReflex#render')
  }
}
