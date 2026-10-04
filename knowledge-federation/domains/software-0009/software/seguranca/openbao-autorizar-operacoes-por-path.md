---
id: software.seguranca.tranche19.001821
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

# OpenBao: Autorizar operações por path

## Em uma frase
**OpenBao — Autorizar operações por path:** Policies OpenBao concedem capabilities a caminhos e permitem limitar o que uma identidade autenticada pode fazer.

## Por que importa
O recorte de **autorizar operações por path** ajuda a controlar credenciais e operações criptográficas com policy-as-code e procedimentos seguros de bootstrap. A equipe registra risco, evidência e responsável.

## Como funciona
Para **autorizar operações por path**, policies HCL autorizam capacidades em caminhos; o estado selado exige procedimento de unseal ou mecanismo automático configurado. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie policy de laboratório com `read` em um único prefixo e sem `list` fora do necessário. Teste em staging autorizado.

## Limites e trade-offs
Caminho genérico pode cobrir mais secrets engines ou namespaces que o pretendido. Exceções exigem responsável e prazo.

## Como verificar
Use token de teste para provar acesso esperado e negar leitura e escrita em caminhos vizinhos. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[openbao-aplicar-menor-privilegio-nas-capabilities]] — Complementa o tópico com openbao: aplicar menor privilégio nas capabilities.

## Fontes
- [OpenBao — Policies](https://openbao.org/docs/concepts/policies/) — documentação oficial de policies HCL, paths e capabilities; consultado em 2026-10-04.
- [OpenBao — Seal and unseal](https://openbao.org/docs/concepts/seal/) — guia oficial do estado sealed, unseal shares e auto-unseal; consultado em 2026-10-04.
