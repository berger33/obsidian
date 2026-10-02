---
id: software.apis.openapi-contrato.000001
tipo: conceito
dominio: software
subdominio: apis
nivel: intermediario
confianca: alta
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://spec.openapis.org/oas/v3.2.1.html", "https://www.rfc-editor.org/rfc/rfc9110.html"]
tags: [dominio/software, subdominio/apis, qualidade/candidata]
aliases: [OpenAPI, Contrato de API HTTP]
---

# OpenAPI como contrato de API HTTP

## Em uma frase
OpenAPI é uma descrição legível por máquinas e pessoas da superfície de uma API HTTP; ela documenta operações e estruturas, mas não prova que a implementação cumpre o contrato.

## Por que importa
Sem um artefato compartilhado, documentação, clientes, testes e implementação podem divergir. Uma descrição OpenAPI revisada permite discutir endpoints, parâmetros, autenticação e respostas antes de publicar uma mudança, além de servir de entrada para geração de documentação, SDKs e validadores.

## Como funciona
Um documento OpenAPI organiza metadados, servidores, caminhos, operações, parâmetros, esquemas de dados, requisitos de segurança e respostas. O `operationId` identifica uma operação e deve ser único no documento. Schemas ajudam a validar formatos, mas não expressam automaticamente todas as regras de negócio, efeitos colaterais, consistência ou compatibilidade de uma API. A especificação descreve APIs HTTP; não obriga, sozinha, uma arquitetura específica de software.

## Exemplo
Uma operação `POST /orders` pode declarar o corpo aceito, os status de sucesso e erro, e o esquema da resposta. O teste da implementação ainda precisa confirmar autorização, persistência, semântica de idempotência e erros reais. Um pipeline pode validar o documento, comparar a versão publicada com a proposta e executar testes de contrato.

## Limites e trade-offs
Uma descrição desatualizada é pior que nenhuma como referência de integração. Gerar código não garante que o código gerado trate corretamente retries, segurança ou regras do negócio. Mudanças no schema também não são todas igualmente incompatíveis: remover um campo, torná-lo obrigatório ou mudar sua semântica pode quebrar clientes mesmo quando o arquivo continua válido.

## Como verificar
Valide o documento com ferramentas compatíveis com a versão declarada, compare-o com rotas implementadas e gere testes para respostas de sucesso e erro. Em revisão, examine compatibilidade com consumidores conhecidos e teste exemplos reais. Separe validação sintática do contrato de testes comportamentais.

## Conexões
- [[idempotencia-http-api]] — semântica HTTP importante que um esquema isolado pode não garantir.
- [[contract-testing-consumer-provider]] — testa interações concretas além da descrição estática.
- [[gates-de-qualidade-no-merge]] — integra validação do contrato à revisão de mudanças.

## Fontes
- [OpenAPI Specification 3.2.1](https://spec.openapis.org/oas/v3.2.1.html) — objetos de operação, parâmetros e respostas; versão publicada consultada em 2026-10-01.
- [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — semântica dos métodos e mensagens HTTP; acesso em 2026-10-01.
