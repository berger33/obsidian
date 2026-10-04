---
id: software.seguranca.tranche18.001732
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

# Kubescape: Executar scan de um control

## Em uma frase
**Kubescape — Executar scan de um control:** Um control pode ser isolado para investigar finding e testar uma correção direcionada.

## Por que importa
O recorte de **executar scan de um control** ajuda a encontrar desvios de configuração antes e depois da implantação com resultados ligados a recursos e controles. A equipe registra risco, evidência e responsável.

## Como funciona
Para **executar scan de um control**, o operador escolhe origem, framework ou control, executa o scan e revisa evidências antes de aplicar remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode o control por id sobre o manifest que gerou a falha, sem substituir o scan integral. Teste em staging autorizado.

## Limites e trade-offs
Execução seletiva não demonstra conformidade com os controles restantes. Exceções exigem responsável e prazo.

## Como verificar
Marque o relatório como parcial e repita framework completo antes do merge final. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubescape-analisar-manifests-locais-antes-do-deploy]] — Complementa o tópico com kubescape: analisar manifests locais antes do deploy.

## Fontes
- [Kubescape — Scanning](https://kubescape.io/docs/scanning/) — documentação oficial de scans de cluster, arquivos, controls, score e exceções; consultado em 2026-10-04.
- [Kubescape — Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/) — catálogo oficial de frameworks e controles de segurança; consultado em 2026-10-04.
