---
id: software.seguranca.tranche17.001605
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

# Trivy: Análise do sistema de arquivos do repositório

## Em uma frase
**Trivy — Análise do sistema de arquivos do repositório:** O alvo `fs` permite examinar uma árvore local e encontrar componentes e arquivos relevantes sem empacotar uma imagem.

## Por que importa
O recorte de **análise do sistema de arquivos do repositório** ajuda a priorizar correções na cadeia de build sem confundir imagem, configuração de IaC e diretório-fonte. A equipe registra risco, evidência e responsável.

## Como funciona
Para **análise do sistema de arquivos do repositório**, seleciona-se primeiro o alvo e depois os scanners adequados; imagens podem conter pacotes, arquivos e configuração de runtime, enquanto arquivos IaC exigem regras próprias. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute `trivy fs` sobre uma cópia limpa do checkout, incluindo lockfiles, para estabelecer um baseline anterior ao build. Teste em staging autorizado.

## Limites e trade-offs
Um diretório não representa necessariamente o conteúdo final da imagem; etapas de build e dependências transitivas podem diferir. Exceções exigem responsável e prazo.

## Como verificar
Compare a lista de arquivos analisados com o checkout e confronte SBOM do build para detectar divergência de escopo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[trivy-scanner-de-licencas-e-inventario]] — Complementa o tópico com trivy: scanner de licenças e inventário.

## Fontes
- [Trivy — Container Image](https://trivy.dev/latest/docs/target/container_image/) — documentação oficial sobre pacotes, configuração de imagem e scanners de vulnerabilidade, segredo e misconfiguração; consultado em 2026-10-04.
- [Trivy — Misconfiguration Scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — documentação oficial sobre IaC e habilitação do scanner de misconfiguração; consultado em 2026-10-04.
