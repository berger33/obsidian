---
id: software.seguranca.tranche18.001740
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

# Kubescape: Publicar resultados JUnit em CI

## Em uma frase
**Kubescape — Publicar resultados JUnit em CI:** Saídas JUnit podem conectar findings ao sistema de testes da pipeline para feedback de merge request.

## Por que importa
O recorte de **publicar resultados junit em ci** ajuda a encontrar desvios de configuração antes e depois da implantação com resultados ligados a recursos e controles. A equipe registra risco, evidência e responsável.

## Como funciona
Para **publicar resultados junit em ci**, o operador escolhe origem, framework ou control, executa o scan e revisa evidências antes de aplicar remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere arquivo JUnit em job que roda em mudanças de manifests e publique o artefato mesmo em falha. Teste em staging autorizado.

## Limites e trade-offs
Formato de relatório não assegura que a etapa falhe por control de segurança. Exceções exigem responsável e prazo.

## Como verificar
Force um finding conhecido e verifique relatório, estado do job e política de threshold. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-linter-comecar-pelos-checks-padroes]] — Complementa o tópico com kubelinter: começar pelos checks padrões.

## Fontes
- [Kubescape — Scanning](https://kubescape.io/docs/scanning/) — documentação oficial de scans de cluster, arquivos, controls, score e exceções; consultado em 2026-10-04.
- [Kubescape — Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/) — catálogo oficial de frameworks e controles de segurança; consultado em 2026-10-04.
