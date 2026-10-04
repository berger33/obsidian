---
id: software.testes.tranche19.001341
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.archunit.org/userguide/html/000_Index.html", "https://javadoc.io/doc/com.tngtech.archunit/archunit/latest/index.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ArchUnit: controlar dependências entre classes e pacotes

## Em uma frase
Regras expressam proibições e permissões de dependência por pacote, nome de classe, anotação ou camada da aplicação.

## Por que importa
Restringir dependências preserva fronteiras de projeto, como impedir que o domínio conheça detalhes de infraestrutura.

## Como funciona
Escreva a regra na negativa, indique explicitamente o motivo e limite o alcance ao conjunto de classes relevante.

## Exemplo
Uma regra pode proibir que classes do domínio dependam de classes do adaptador de persistência.

## Limites e trade-offs
Regras amplas demais acusam dependências legítimas e são desativadas, enquanto regras estreitas deixam caminhos relevantes fora.

## Como verificar
Crie uma dependência proibida em código de teste e confirme que a regra falha com a mensagem de motivo declarada.

## Conexões
- [[archunit-slices-and-cycles]] — Veja também: ArchUnit: detectar dependências cíclicas.
- [[archunit-coding-rules]] — Veja também: ArchUnit: aplicar convenções de codificação.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — Documentação de API](https://javadoc.io/doc/com.tngtech.archunit/archunit/latest/index.html) — referência das classes de regras e da API de camadas; consultado em 2026-10-03.
