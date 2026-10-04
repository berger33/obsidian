---
id: software.seguranca.tranche17.001606
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

# Trivy: Scanner de licenças e inventário

## Em uma frase
**Trivy — Scanner de licenças e inventário:** A identificação de licenças é uma classe de inspeção distinta da detecção de CVEs e pode ser tratada em uma política própria.

## Por que importa
O recorte de **scanner de licenças e inventário** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **scanner de licenças e inventário**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere um relatório de licença para um artefato de teste e encaminhe componentes sem licença reconhecida para triagem jurídica. Teste em staging autorizado.

## Limites e trade-offs
Licença detectada automaticamente pode ser ausente, ambígua ou derivada de metadados; o relatório não substitui revisão legal. Exceções exigem responsável e prazo.

## Como verificar
Valide amostras conhecidas do inventário e registre como a organização resolve licenças desconhecidas e arquivos vendorizados. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-relatorios-json-e-sarif-em-ci]] — Complementa o tópico com trivy: relatórios json e sarif em ci.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
