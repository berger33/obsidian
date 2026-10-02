---
id: software.testes.tranche09.000296
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://developer.apple.com/documentation/xctest/xctossignpostmetric", "https://developer.apple.com/documentation/xctest/performance-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# XCTest: medir intervalo instrumentado com signpost metric

## Em uma frase
XCTOSSignpostMetric mede duração de regiões marcadas por signposts, aproximando o intervalo definido pela instrumentação da aplicação.

## Por que importa
XCTest oferece APIs diferentes para Swift async/await, callbacks, interface e medição; escolher a API adequada reduz sincronização artificial. Medir a suite inteira pode misturar inicialização, setup e trabalho do produto e atribuir regressão à etapa errada.

## Como funciona
Prepare estado em cada caso, aguarde eventos ou condições observáveis e associe métricas aos intervalos que representam o custo medido. Coloque signposts ao redor da operação de interesse e associe a métrica ao teste de performance que a repete.

## Exemplo
Uma busca local mede a região de consulta e renderização marcada, sem incluir login do simulador no baseline.

## Limites e trade-offs
Simuladores, devices, configurações e dependências externas variam; resultados de UI e performance exigem ambiente registrado e expectativas realistas. Signpost ausente ou mal delimitado invalida a comparação; hardware e build continuam influenciando os valores.

## Como verificar
Confirme eventos de início/fim em Instruments e compare execuções no mesmo destino e configuração de build.

## Conexões
- [[xctest-plans-matrix-configurations]] — Veja também: Xcode test plans: variar configurações de execução intencionalmente.
- [[xctest-order-independent-state-reset]] — Veja também: XCTest: não depender da ordem dos métodos de teste.

## Fontes
- [Apple — XCTOSSignpostMetric](https://developer.apple.com/documentation/xctest/xctossignpostmetric) — medição de intervalos instrumentados por signposts; consultado em 2026-10-02.
- [Apple — Performance tests](https://developer.apple.com/documentation/xctest/performance-tests) — medição repetível de performance em testes XCTest; consultado em 2026-10-02.
