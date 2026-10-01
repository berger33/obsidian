---
tipo: ficha
status: semente
camada: ponte
hub: "[[MOC - Desenvolvimento de Jogos 2D]]"
tags: [jogos2d, arquitetura, padroes]
conexoes_chave: ["[[Coesão e acoplamento]]", "[[Game loop]]", "[[Sistemas determinísticos]]", "[[IA de inimigos 2D]]"]
---

# ECS

#jogos2d #arquitetura #padroes

## Resumo
Organiza entidades por composição de componentes e sistemas, favorecendo flexibilidade e performance em certos contextos.

## Pergunta que esta nota responde
O comportamento deve nascer de hierarquias de classes ou da combinação de componentes?

## Definição operacional
Entity Component System separa identidade, dados e processamento. Entidades são IDs, componentes guardam dados e sistemas processam conjuntos de componentes. É poderoso, mas pode ser excesso para projetos simples.

## Quando usar
- Quando há muitas entidades similares com combinações variadas.
- Quando composição supera herança.
- Quando performance de processamento em lote importa.

## Sinais de boa aplicação
- Componentes são dados simples.
- Sistemas têm responsabilidade clara.
- A arquitetura não sacrifica legibilidade sem ganho real.

## Conexões
- [[Coesão e acoplamento]]
- [[Game loop]]
- [[Sistemas determinísticos]]
- [[IA de inimigos 2D]]
- [[Colisão 2D]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Desenvolvimento de Jogos 2D]].
