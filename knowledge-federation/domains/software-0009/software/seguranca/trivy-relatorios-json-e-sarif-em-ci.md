---
id: software.seguranca.tranche17.001607
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://trivy.dev/latest/docs/target/container_image/", "https://trivy.dev/latest/docs/scanner/misconfiguration/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Trivy: Relatórios JSON e SARIF em CI

## Em uma frase
**Trivy — Relatórios JSON e SARIF em CI:** Saídas estruturadas permitem integrar achados ao fluxo de revisão sem depender apenas da apresentação em terminal.

## Por que importa
O recorte de **relatórios json e sarif em ci** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **relatórios json e sarif em ci**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em uma branch de teste, exporte JSON ou SARIF e associe cada finding ao commit e ao digest escaneado. Teste em staging autorizado.

## Limites e trade-offs
O formato de saída não melhora cobertura nem assegura que um consumidor interprete corretamente severidade e supressões. Exceções exigem responsável e prazo.

## Como verificar
Valide o schema e faça um teste ponta a ponta que demonstre a presença de um finding conhecido no sistema consumidor. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-excecoes-de-vulnerabilidade-com-justificativa]] — Complementa o tópico com trivy: exceções de vulnerabilidade com justificativa.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
