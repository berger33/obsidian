---
id: software.testes.tranche08.000176
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://developer.android.com/training/testing/fundamentals", "https://developer.android.com/training/testing/different-screens"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Android: testar restauração após recriação do processo

## Em uma frase
Trate rotação e morte de processo como eventos distintos e valide qual estado o produto promete recuperar.

## Por que importa
A recriação de Activity pode preservar estado por caminhos diferentes de uma interrupção do processo; confundi-los deixa perdas de dados sem teste.

## Como funciona
Defina dados transitórios e persistidos, acione o ciclo de vida relevante e verifique restauração pela interface ou armazenamento esperado.

## Exemplo
Um rascunho não enviado sobrevive à rotação; em outro cenário, o processo é recriado e o app recupera apenas o estado que o requisito exige.

## Limites e trade-offs
A automação de emulador não reproduz toda política de memória do sistema em dispositivos reais; não atribua garantia além do lifecycle testado.

## Como verificar
Observe estado antes e depois de cada evento, teste retorno após background e diferencie estado salvo de dados deliberadamente descartados.

## Conexões
- [[android-multiplas-telas-configuracao]] — Veja também: Android: cobrir tamanhos de tela e configuração.
- [[android-separar-teste-ui-de-regra]] — Veja também: Android: não concentrar regras de negócio em teste de UI.

## Fontes
- [Android — Fundamentals of testing](https://developer.android.com/training/testing/fundamentals) — escopo, ambiente e tipos de teste Android; consultado em 2026-10-02.
- [Android — Different screen sizes](https://developer.android.com/training/testing/different-screens) — tamanhos de tela, configuração e restauração de estado; consultado em 2026-10-02.
