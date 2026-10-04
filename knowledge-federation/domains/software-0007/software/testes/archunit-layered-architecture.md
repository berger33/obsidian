---
id: software.testes.tranche19.001339
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

# ArchUnit: verificar arquitetura em camadas

## Em uma frase
Regras de camadas definem grupos por padrão de pacote e restringem quais camadas podem acessar quais outras.

## Por que importa
A verificação impede atalhos entre camadas, como acesso direto da interface à persistência, que corroem a separação ao longo do tempo.

## Como funciona
Nomeie as camadas pelas responsabilidades reais, declare as regras de acesso permitido e documente o motivo de cada restrição.

## Exemplo
Uma regra pode permitir que serviços sejam acessados apenas por controladores e que a persistência seja acessada apenas por serviços.

## Limites e trade-offs
Camadas definidas por padrões amplos incluem classes indevidas, e regras desatualizadas passam a apontar violações que já não fazem sentido.

## Como verificar
Introduza um acesso proibido entre camadas em código de teste e confirme que a regra falha indicando a classe e a dependência.

## Conexões
- [[archunit-import-and-rules]] — Veja também: ArchUnit: importar o código e declarar regras.
- [[archunit-slices-and-cycles]] — Veja também: ArchUnit: detectar dependências cíclicas.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — Documentação de API](https://javadoc.io/doc/com.tngtech.archunit/archunit/latest/index.html) — referência das classes de regras e da API de camadas; consultado em 2026-10-03.
