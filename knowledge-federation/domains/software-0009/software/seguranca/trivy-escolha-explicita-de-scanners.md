---
id: software.seguranca.tranche17.001602
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

# Trivy: Escolha explícita de scanners

## Em uma frase
**Trivy — Escolha explícita de scanners:** Os scanners de vulnerabilidade e segredos são habilitados por padrão para imagem; misconfiguração precisa de seleção específica para vários subcomandos.

## Por que importa
O recorte de **escolha explícita de scanners** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolha explícita de scanners**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Para IaC no diretório `infra/`, prefira `trivy config infra/`; não suponha que `trivy image` aplique todas as verificações de configuração automaticamente. Teste em staging autorizado.

## Limites e trade-offs
Um scanner não cobre os objetivos dos demais; habilitar vulnerabilidade não equivale a executar avaliação de IaC ou licença. Exceções exigem responsável e prazo.

## Como verificar
Registre subcomando e lista de scanners e confirme, em saída controlada, que cada classe esperada foi efetivamente executada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-misconfiguracao-em-terraform-e-kubernetes]] — Complementa o tópico com trivy: misconfiguração em terraform e kubernetes.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
