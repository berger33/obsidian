---
id: software.testes.tranche15.000906
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/extensions/simple-extensions.html", "https://kotest.io/docs/framework/isolation-mode.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: escolher listener de setup conforme o número de instâncias

## Em uma frase
Hooks e extensions podem ser chamados uma vez por classe ou para cada instância, distinção importante quando `InstancePerRoot` recria a Spec para grupos diferentes.

## Por que importa
`BeforeSpecListener` acompanha cada instância criada; `PrepareSpecListener` é chamado uma vez por Spec antes da execução dos casos, mesmo se o engine fizer várias instâncias.

## Como funciona
O hook certo impede inicialização repetida de recurso que deveria ser única ou recurso sem setup na nova instância.

## Exemplo
Use preparação por instância para um cliente guardado em campo da Spec e listener de preparação da Spec para uma operação realmente compartilhada, mantendo cleanup no callback com lifecycle correspondente.

## Limites e trade-offs
A escolha depende do isolation mode e da visibilidade do recurso; estado global continua exigindo coordenação e liberação mesmo que o listener rode uma vez.

## Como verificar
Registre a contagem de callbacks num teste com duas raízes e compare BeforeSpecListener com PrepareSpecListener ao alternar o isolation mode.

## Conexões
- [[kotest-shared-test-config-com-defaults-locais]] — Veja também: Kotest 6.2: centralizar defaults sem impedir ajustes por caso.
- [[kotest-platforms-defaults-de-concorrencia]] — Veja também: Kotest 6.2: evitar aplicar expectativa JVM a todas as plataformas.

## Fontes
- [Kotest 6.2 — Simple Extensions](https://kotest.io/docs/framework/extensions/simple-extensions.html) — listeners de lifecycle por instância ou spec; consultado em 2026-10-02.
- [Kotest 6.2 — Isolation Modes](https://kotest.io/docs/framework/isolation-mode.html) — instâncias de Spec, SingleInstance, InstancePerRoot e modos depreciados; consultado em 2026-10-02.
