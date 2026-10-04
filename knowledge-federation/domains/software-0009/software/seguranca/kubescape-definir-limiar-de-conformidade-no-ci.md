---
id: software.seguranca.tranche18.001736
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

# Kubescape: Definir limiar de conformidade no CI

## Em uma frase
**Kubescape — Definir limiar de conformidade no CI:** A opção de threshold pode falhar um job quando o score de um framework ou control fica abaixo do valor escolhido.

## Por que importa
O recorte de **definir limiar de conformidade no ci** ajuda a encontrar desvios de configuração antes e depois da implantação com resultados ligados a recursos e controles. A equipe registra risco, evidência e responsável.

## Como funciona
Para **definir limiar de conformidade no ci**, o operador escolhe origem, framework ou control, executa o scan e revisa evidências antes de aplicar remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use framework scan com threshold após observar baseline de um ambiente controlado. Teste em staging autorizado.

## Limites e trade-offs
Limiar numérico pode esconder um control crítico se a equipe tratar o score como aprovação única. Exceções exigem responsável e prazo.

## Como verificar
Teste um recurso que falha e confirme que o processo retorna código de saída não zero. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubescape-governar-excecoes-de-findings]] — Complementa o tópico com kubescape: governar exceções de findings.

## Fontes
- [Kubescape — Scanning](https://kubescape.io/docs/scanning/) — documentação oficial de scans de cluster, arquivos, controls, score e exceções; consultado em 2026-10-04.
- [Kubescape — Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/) — catálogo oficial de frameworks e controles de segurança; consultado em 2026-10-04.
