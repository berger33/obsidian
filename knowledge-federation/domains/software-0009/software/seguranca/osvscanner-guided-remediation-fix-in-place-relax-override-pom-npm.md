---
id: software.seguranca.tranche01.000025
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/google/osv-scanner/main/README.md", "https://google.github.io/osv-scanner/usage/", "https://github.com/google/osv-scanner"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OSV-Scanner Guided Remediation (`osv-scanner fix`): estratégias `in-place`, `relax` e `override` para atualização segura de dependências

## Em uma frase
O subcomando **`osv-scanner fix`** (*Guided Remediation*) calcula automaticamente as atualizações de versão de pacotes com melhor retorno sobre investimento (considerando profundidade da dependência, severidade mínima, compatibilidade semver e número de CVEs resolvidas) para `package.json` / `package-lock.json` (**npm**) e `pom.xml` (**Maven**).

## Por que importa
Atualizar cegamente todas as dependências para a versão `latest` com `npm audit fix --force` frequentemente introduz *breaking changes* de versão maior (`major`); já corrigir dependências transitivas profundas manualmente em um `pom.xml` exige tentativa e erro demorada.

## Como funciona
O `osv-scanner fix` suporta três estratégias explícitas: 1) **`in-place`** (atualiza versões diretamente dentro do `package-lock.json` respeitando as restrições atuais do `package.json`); 2) **`relax`** (relaxa as constraints de versão no `package.json` apenas o necessário para eliminar a CVE); e 3) **`override`** (adiciona entradas em `<dependencyManagement>` no `pom.xml` do Maven para forçar versões seguras de dependências transitivas).

## Exemplo
```bash
# Calculando e aplicando correções guiadas em um projeto npm sem breaking changes desnecessárias:
osv-scanner fix -M ./package.json -L ./package-lock.json
```

## Limites e trade-offs
Conforme o alerta de segurança oficial na documentação do OSV-Scanner, **nunca** execute `osv-scanner fix` em repositórios não confiáveis, pois a resolução pelo gerenciador de pacotes pode acionar scripts de ciclo de vida ou consultar registries externos definidos no projeto.

## Como verificar
Execute `osv-scanner fix --help` para revisar as flags de estratégia (`--strategy`), severidade mínima e profundidade de dependência.

## Conexões
- [[osvscanner-call-analysis-reachability-go-rust-reducao-falsos-positivos]] — Veja também: OSV-Scanner Call Analysis (*Reachability*): análise de grafo de chamadas para verificar se a função vulnerável é realmente invocada.
- [[osvscanner-license-scanning-deps-dev-spdx-allowlist-compliance]] — Veja também: OSV-Scanner License Scanning (`--licenses`): auditoria de licenças de software livre via `deps.dev` e validação contra allowlist SPDX.

## Fontes
- [Google OSV-Scanner GitHub — README.md (OSV-Scanner V2 Features, OSV-Scalibr Engine, Container Scanning, Call Analysis & Guided Remediation)](https://raw.githubusercontent.com/google/osv-scanner/main/README.md) — README oficial do google/osv-scanner descrevendo a arquitetura V2 baseada no OSV-Scalibr, suporte a lockfiles/SBOMs, imagens de container e remediação guiada; consultado em 2026-10-03.
- [OSV-Scanner Official Documentation — Usage & Configuration (scan source, scan image, fix Strategies, --licenses, Offline DB & osv-scanner.toml)](https://google.github.io/osv-scanner/usage/) — Documentação oficial de uso do OSV-Scanner detalhando flags de CLI, estratégias de osv-scanner fix (in-place, relax, override), auditoria SPDX e osv-scanner.toml; consultado em 2026-10-03.
- [Google OSV-Scanner — Official GitHub Repository](https://github.com/google/osv-scanner) — Repositório oficial Apache-2.0 do Google OSV-Scanner; consultado em 2026-10-03.
