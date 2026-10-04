---
id: software.seguranca.tranche18.001737
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

# Kubescape: Governar exceções de findings

## Em uma frase
**Kubescape — Governar exceções de findings:** Exceções permitem aceitar risco conhecido e devem ter escopo explícito em vez de remover o finding do inventário.

## Por que importa
O recorte de **governar exceções de findings** ajuda a encontrar desvios de configuração antes e depois da implantação com resultados ligados a recursos e controles. A equipe registra risco, evidência e responsável.

## Como funciona
Para **governar exceções de findings**, o operador escolhe origem, framework ou control, executa o scan e revisa evidências antes de aplicar remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Associe uma exceção a recurso e control específicos em ambiente de teste. Teste em staging autorizado.

## Limites e trade-offs
Exceção ampla pode persistir após recurso, imagem ou risco mudar. Exceções exigem responsável e prazo.

## Como verificar
Revise arquivo de exceções, responsável, justificativa e expiração em cada release. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubescape-interpretar-remediacao-assistida]] — Complementa o tópico com kubescape: interpretar remediação assistida.

## Fontes
- [Kubescape — Scanning](https://kubescape.io/docs/scanning/) — documentação oficial de scans de cluster, arquivos, controls, score e exceções; consultado em 2026-10-04.
- [Kubescape — Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/) — catálogo oficial de frameworks e controles de segurança; consultado em 2026-10-04.
