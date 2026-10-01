---
tipo: ficha
status: semente
camada: software
hub: "[[MOC - Engenharia de Software]]"
tags: [software, arquitetura, qualidade]
conexoes_chave: ["[[Monólito modular]]", "[[Arquitetura em camadas]]", "[[ECS]]", "[[Refatoração]]"]
---

# Coesão e acoplamento

#software #arquitetura #qualidade

## Resumo
Critério central para decidir se uma parte do sistema deve ficar junto ou separada.

## Pergunta que esta nota responde
O que muda junto deve morar junto? O que muda por motivos diferentes está separado?

## Definição operacional
Coesão mede o quanto os elementos de um módulo pertencem ao mesmo propósito. Acoplamento mede o quanto um módulo depende de detalhes de outro. Bons sistemas têm alta coesão e baixo acoplamento intencional.

## Quando usar
- Ao refatorar classes grandes.
- Ao criar sistemas independentes de gameplay.
- Ao avaliar fronteiras entre módulos.

## Sinais de boa aplicação
- Mudanças pequenas não atravessam muitas pastas.
- Dependências apontam para abstrações estáveis.
- O grafo de notas mostra clusters claros, não um centro único inchado.

## Conexões
- [[Monólito modular]]
- [[Arquitetura em camadas]]
- [[ECS]]
- [[Refatoração]]
- [[Dívida técnica]]

## Próximas pesquisas
- Procurar exemplos práticos em engines 2D como Godot, Unity ou frameworks customizados.
- Registrar um [[Registro de decisões arquiteturais]] quando esta ideia virar escolha de projeto.
- Conectar novos aprendizados ao hub [[MOC - Engenharia de Software]].
