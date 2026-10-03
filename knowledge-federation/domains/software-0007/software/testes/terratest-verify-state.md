---
id: software.testes.tranche19.001303
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform", "https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/aws"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terratest: verificar o estado real após aplicar

## Em uma frase
Depois da aplicação, os auxiliares consultam o provedor para confirmar que o recurso existe e apresenta as propriedades esperadas, em vez de confiar apenas na saída declarada.

## Por que importa
A consulta ao estado real detecta diferenças entre o que a configuração promete e o que foi efetivamente criado.

## Como funciona
Leia as saídas, consulte o provedor e compare as propriedades relevantes do recurso, como criptografia e bloqueio de acesso público.

## Exemplo
Um teste pode confirmar que o depósito criado tem versionamento ativo e acesso público bloqueado conforme declarado.

## Limites e trade-offs
Verificar apenas a saída da configuração não detecta recurso que o provedor ajustou ou rejeitou parcialmente.

## Como verificar
Remova uma propriedade da configuração e confirme que a verificação de estado passa a falhar, provando que ela observa o recurso real.

## Conexões
- [[terratest-unique-resources]] — Veja também: Terratest: gerar nomes únicos para recursos.
- [[terratest-http-checks]] — Veja também: Terratest: verificar o serviço implantado.

## Fontes
- [Terratest — Módulo terraform](https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform) — opções, aplicação, saídas e destruição; consultado em 2026-10-03.
- [Terratest — Módulo aws](https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/aws) — consultas de estado e verificação de recursos; consultado em 2026-10-03.
