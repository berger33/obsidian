---
id: software.testes.tranche20.001443
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://robolectric.org/getting-started/", "https://robolectric.org/configuring/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robolectric: usar recursos e qualificadores

## Em uma frase
A execução carrega recursos do projeto e permite escolher qualificadores, como idioma, orientação e densidade de tela.

## Por que importa
Recursos diferentes mudam textos e layouts, e verificar apenas a configuração padrão deixa variações importantes sem cobertura.

## Como funciona
Habilite o carregamento de recursos do Android, escolha os qualificadores por caso e verifique textos obtidos do recurso em vez de fixos.

## Exemplo
Um caso pode rodar com idioma diferente e confirmar que a tela exibe o texto traduzido correspondente ao recurso.

## Limites e trade-offs
Textos fixos no teste deixam de acompanhar os recursos, e esquecer de habilitar o carregamento gera recursos ausentes em execução.

## Como verificar
Troque o qualificador de idioma e confirme que o texto verificado acompanha o recurso carregado.

## Conexões
- [[robolectric-activity-lifecycle]] — Veja também: Robolectric: controlar o ciclo de vida de telas.
- [[robolectric-java-version-compatibility]] — Veja também: Robolectric: ajustar a JVM de execução.

## Fontes
- [Robolectric — Primeiros passos](https://robolectric.org/getting-started/) — configuração do projeto, executor e ciclo de vida de telas; consultado em 2026-10-03.
- [Robolectric — Configuração](https://robolectric.org/configuring/) — versão de sistema, sombras, propriedades e repositórios; consultado em 2026-10-03.
