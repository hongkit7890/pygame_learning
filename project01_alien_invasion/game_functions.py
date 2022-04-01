import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings,screen,ship,bullets):
    """Respond to keypresses and mouse events."""
	
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      elif event.type==pygame.KEYDOWN:
        check_keydown_events(event,ai_settings,screen,ship,bullets)

      elif event.type == pygame.KEYUP:
        check_keyup_events(event,ship)



      

def check_keydown_events(event,ai_settings,screen,ship,bullets):
  if event.key == pygame.K_RIGHT:
    #Move the ship to the right.
    ship.moving_right = True
  if event.key == pygame.K_LEFT:
    #Move the ship to the left.
    ship.moving_left = True
  elif event.key == pygame.K_SPACE:
    fire_bullet(ai_settings, screen,ship,bullets)
  elif event.key == pygame.K_q:
    sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
  #create len(bullets) < ai_settings.bullets_allowed:
  if len(bullets) < ai_settings.bullets_allowed:
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)

def check_keyup_events(event,ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  if event.key == pygame.K_LEFT:
    ship.moving_left = False
	
def update_screen(ai_settings,screen,alien,ship,bullets):
    """Update images on the screen and flip to the new screen"""
    #Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme() 
    
    
    for bullet in bullets.sprites():
      bullet.draw_bullet()

    
    aliens.draw(screen)

    #Make the most recently draw screen visible.
    pygame.display.flip()


    
def update_bullets(bullets):
  """Update position of bullets and get rid of old bullets."""
  #Update Bullet positions
  bullets.update()

  #Get rid of bullets that hae disappeared
  for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
      bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
  """Create a full fleet of aliens."""
  # Create an alien and find the number of aliens in a row.
  # Spacing between each alien is equal to one alien width.
  alien = Alien(ai_settings, screen)
  alien_width = alien.rect.width
  available_space_x = ai_settings.screen_width - 2 * alien_width
  number_aliens_x = int(available_space_x / (2 * alien_width))
  
  
  # Create the first row of aliens.
  for alien_number in range(number_aliens_x):
    # Create an alien and place it in the row.
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
  "Respond appropriately if any aliens have reached an edge."""
   for alien in aliens.sprites():
    if alien.check_edges():
      change_fleet_direction(ai_settings, aliens)
      break


def change_fleet_direction(ai_settings, aliens):
"""Drop the entire fleet and change the fleet's direction."""
for alien in aliens.sprites():
v alien.rect.y += ai_settings.fleet_drop_speed
ai_settings.fleet_direction *= -1