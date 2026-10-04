---
id: software.seguranca.tranche19.001822
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-19.md"
fontes: ["https://openbao.org/docs/concepts/policies/", "https://openbao.org/docs/concepts/seal/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenBao: Aplicar menor privilégio nas capabilities

## Em uma frase
**OpenBao — Aplicar menor privilégio nas capabilities:** Capabilities como read, create, update, delete e list devem corresponder à tarefa do cliente.

## Por que importa
O recorte de **aplicar menor privilégio nas capabilities** ajuda a controlar credenciais e operações criptográficas com policy-as-code e procedimentos seguros de bootstrap. A equipe registra risco, evidência e responsável.

## Como funciona
Para **aplicar menor privilégio nas capabilities**, policies HCL autorizam capacidades em caminhos; o estado selado exige procedimento de unseal ou mecanismo automático configurado. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Separe policy de leitura de aplicação da policy administrativa de rotação. Teste em staging autorizado.

## Limites e trade-offs
`sudo` ou capabilities amplas podem ultrapassar a fronteira de path prevista. Exceções exigem responsável e prazo.

## Como verificar
Audite capabilities concedidas e use cliente com cada policy para testar ações negativas. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openbao-entender-policy-deny-e-composicao]] — Complementa o tópico com openbao: entender policy deny e composição.

## Fontes
- [OpenBao — Policies](https://openbao.org/docs/concepts/policies/) — documentação oficial de policies HCL, paths e capabilities; consultado em 2026-10-04.
- [OpenBao — Seal and unseal](https://openbao.org/docs/concepts/seal/) — guia oficial do estado sealed, unseal shares e auto-unseal; consultado em 2026-10-04.
