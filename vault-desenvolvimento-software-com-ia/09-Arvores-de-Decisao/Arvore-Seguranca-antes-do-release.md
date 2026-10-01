---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Seguranca antes do release"]
---
# Seguranca antes do release

## Pergunta inicial
Seguranca antes do release?

## Versão em texto
- **Auth** → [[Autenticacao]]
- **Input** → [[OWASP-Top-10]]
- **Secrets** → [[Secrets-management]]
- **LLM** → [[Seguranca-em-apps-com-LLM]]

## Diagrama
```mermaid
flowchart TD
    A[Seguranca antes do release]
    A --> B1[Auth]
    B1 --> L1[[Autenticacao]]
    A --> B2[Input]
    B2 --> L2[[OWASP-Top-10]]
    A --> B3[Secrets]
    B3 --> L3[[Secrets-management]]
    A --> B4[LLM]
    B4 --> L4[[Seguranca-em-apps-com-LLM]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
