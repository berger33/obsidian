---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["MMO e viavel para uma pessoa"]
---
# MMO e viavel para uma pessoa

## Pergunta inicial
MMO e viavel para uma pessoa?

## Versão em texto
- **Sem comunidade** → [[MMO-para-solo-dev]]
- **Protótipo social** → [[Servidor-autoritativo]]
- **Servidor caro** → [[Custos-de-nuvem]]
- **Live ops** → [[Live-ops-para-jogos]]

## Diagrama
```mermaid
flowchart TD
    A[MMO e viavel para uma pessoa]
    A --> B1[Sem comunidade]
    B1 --> L1[[MMO-para-solo-dev]]
    A --> B2[Protótipo social]
    B2 --> L2[[Servidor-autoritativo]]
    A --> B3[Servidor caro]
    B3 --> L3[[Custos-de-nuvem]]
    A --> B4[Live ops]
    B4 --> L4[[Live-ops-para-jogos]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
