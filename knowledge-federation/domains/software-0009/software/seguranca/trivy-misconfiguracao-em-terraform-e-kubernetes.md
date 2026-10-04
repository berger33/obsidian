---
id: software.seguranca.tranche17.001603
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

# Trivy: Misconfiguração em Terraform e Kubernetes

## Em uma frase
**Trivy — Misconfiguração em Terraform e Kubernetes:** O scanner de configuração avalia definições IaC, como Terraform, CloudFormation, templates Helm e Dockerfiles, contra checks publicados.

## Por que importa
O recorte de **misconfiguração em terraform e kubernetes** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **misconfiguração em terraform e kubernetes**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode `trivy config` sobre uma fixture de teste com uma configuração insegura conhecida e valide que a regra aponta arquivo e linha. Teste em staging autorizado.

## Limites e trade-offs
Um check estático não demonstra que o recurso esteja implantado nem considera necessariamente variáveis resolvidas em runtime. Exceções exigem responsável e prazo.

## Como verificar
Teste regras em fixtures boas e ruins e confirme caminho, regra e severidade antes de bloquear o pipeline. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-segredos-na-configuracao-da-imagem]] — Complementa o tópico com trivy: segredos na configuração da imagem.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
