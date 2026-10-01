---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Usar modelo local ou nuvem"]
---
# Usar modelo local ou nuvem

## Pergunta inicial
Usar modelo local ou nuvem?

## Versão em texto
- **Privacidade** → [[Modelos-locais]]
- **Máxima capacidade** → [[Modelos-em-nuvem]]
- **Custo previsível** → [[Custos-de-tokens]]
- **Sem GPU** → [[Cloud-agent]]

## Diagrama
```mermaid
flowchart TD
    A[Usar modelo local ou nuvem]
    A --> B1[Privacidade]
    B1 --> L1[[Modelos-locais]]
    A --> B2[Máxima capacidade]
    B2 --> L2[[Modelos-em-nuvem]]
    A --> B3[Custo previsível]
    B3 --> L3[[Custos-de-tokens]]
    A --> B4[Sem GPU]
    B4 --> L4[[Cloud-agent]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
