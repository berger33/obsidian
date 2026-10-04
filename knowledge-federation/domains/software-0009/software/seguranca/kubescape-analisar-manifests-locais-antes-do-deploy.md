---
id: software.seguranca.tranche18.001733
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://kubescape.io/docs/scanning/", "https://kubescape.io/docs/frameworks-and-controls/frameworks/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Kubescape: Analisar manifests locais antes do deploy

## Em uma frase
**Kubescape — Analisar manifests locais antes do deploy:** Kubescape pode examinar arquivos YAML ou JSON e apontar o recurso de origem associado ao control.

## Por que importa
O recorte de **analisar manifests locais antes do deploy** ajuda a encontrar desvios de configuração antes e depois da implantação com resultados ligados a recursos e controles. A equipe registra risco, evidência e responsável.

## Como funciona
Para **analisar manifests locais antes do deploy**, o operador escolhe origem, framework ou control, executa o scan e revisa evidências antes de aplicar remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Escaneie diretório versionado de manifests no pull request antes de aplicar ao cluster. Teste em staging autorizado.

## Limites e trade-offs
Arquivo de entrada não inclui necessariamente valores renderizados ou estado efetivo do cluster. Exceções exigem responsável e prazo.

## Como verificar
Compare o arquivo analisado com o artefato renderizado que a pipeline planeja aplicar. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubescape-examinar-cluster-com-kubeconfig-definido]] — Complementa o tópico com kubescape: examinar cluster com kubeconfig definido.

## Fontes
- [Kubescape — Scanning](https://kubescape.io/docs/scanning/) — documentação oficial de scans de cluster, arquivos, controls, score e exceções; consultado em 2026-10-04.
- [Kubescape — Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/) — catálogo oficial de frameworks e controles de segurança; consultado em 2026-10-04.
