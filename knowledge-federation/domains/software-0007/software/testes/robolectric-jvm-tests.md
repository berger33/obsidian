---
id: software.testes.tranche20.001439
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
fontes: ["https://robolectric.org/getting-started/", "https://github.com/robolectric/robolectric"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robolectric: rodar testes Android na JVM

## Em uma frase
A ferramenta executa código Android na máquina virtual da linguagem, substituindo chamadas ao sistema por implementações próprias.

## Por que importa
Testar na JVM elimina a necessidade de emulador ou aparelho, tornando a suíte rápida o bastante para rodar a cada alteração.

## Como funciona
Configure o módulo com recursos do Android e a dependência de teste, anote a classe com o executor e escreva casos comuns de teste.

## Exemplo
Um teste de regra de tela pode rodar na JVM em milissegundos, sem subir emulador nem esperar a instalação do aplicativo.

## Limites e trade-offs
Nem todo comportamento do dispositivo é reproduzido, e caminhos que dependem de hardware real exigem verificação em aparelho.

## Como verificar
Compare o tempo da mesma verificação na JVM e em execução instrumentada para dimensionar o ganho obtido.

## Conexões
- [[robolectric-sdk-configuration]] — Veja também: Robolectric: escolher a versão de sistema.

## Fontes
- [Robolectric — Primeiros passos](https://robolectric.org/getting-started/) — configuração do projeto, executor e ciclo de vida de telas; consultado em 2026-10-03.
- [Robolectric — repositório oficial](https://github.com/robolectric/robolectric) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
