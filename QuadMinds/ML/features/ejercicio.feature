Feature: En este feature se encontraran los escenarios correspondientes a la prueba del ejercicio de "Mercado Libre"


  @ejercicio
  Scenario Outline: : Este escenario se encargara de Verificar el último producto de la Categoria Tecnología -> Computación -> Componentes de PC.
    Given Ingresar al Sitio de Mercado Libre
    When Ir a la Categoria Tecnologia -> Computacion -> Componentes de PC
    And Filtrar por <ciudad> e Informar la Cantidad Listada.
    And Informar los Datos de la Ultima Publicacion y acceder
    Then Verificar los datos de la Publicacion


    Examples:
    |ciudad         |
    |Capital Federal|