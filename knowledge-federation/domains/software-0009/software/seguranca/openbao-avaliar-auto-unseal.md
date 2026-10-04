---
id: software.seguranca.tranche19.001828
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

# OpenBao: Avaliar auto-unseal

## Em uma frase
**OpenBao — Avaliar auto-unseal:** Auto-unseal delega proteção a um serviço externo de chaves e altera requisitos de disponibilidade e recuperação.

## Por que importa
O recorte de **avaliar auto-unseal** ajuda a controlar credenciais e operações criptográficas com policy-as-code e procedimentos seguros de bootstrap. A equipe registra risco, evidência e responsável.

## Como funciona
Para **avaliar auto-unseal**, policies HCL autorizam capacidades em caminhos; o estado selado exige procedimento de unseal ou mecanismo automático configurado. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Teste integração com KMS dedicado e identidade de serviço de menor privilégio em staging. Teste em staging autorizado.

## Limites e trade-offs
Falha do KMS pode impedir recuperação ou inicialização do serviço. Exceções exigem responsável e prazo.

## Como verificar
Teste permissão negada, indisponibilidade temporária e restauração com plano documentado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openbao-planejar-recuperacao-sem-divulgar-shares]] — Complementa o tópico com openbao: planejar recuperação sem divulgar shares.

## Fontes
- [OpenBao — Policies](https://openbao.org/docs/concepts/policies/) — documentação oficial de policies HCL, paths e capabilities; consultado em 2026-10-04.
- [OpenBao — Seal and unseal](https://openbao.org/docs/concepts/seal/) — guia oficial do estado sealed, unseal shares e auto-unseal; consultado em 2026-10-04.
