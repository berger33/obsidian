---
id: software.devops.tranche07.000643
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/kubescape/kubescape/master/README.md", "https://kubescape.io/docs/operator/", "https://github.com/kubescape/kubescape"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kubescape: auto-remediação de manifestos (kubescape fix) e patching de imagens com Copacetic (kubescape patch)

## Em uma frase
O Kubescape vai além da detecção ao corrigir automaticamente configurações inseguras em manifestos YAML (`kubescape fix`) e aplicar patches de segurança em imagens de container vulneráveis usando o Copacetic e BuildKit (`kubescape patch`).

## Por que importa
Relatórios de segurança que apenas listam centenas de falhas de configuração YAML e CVEs de sistema operacional frequentemente acumulam backlog porque os desenvolvedores precisam descobrir manualmente qual campo adicionar no Deployment ou aguardar a equipe base reconstruir um Dockerfile inteiro. Segundo o README oficial do Kubescape, os subcomandos `fix` e `patch` automatizam a remediação tanto na camada de configuração quanto na camada de imagem OCI.

## Como funciona
Para auto-remediação de manifestos, o usuário primeiro executa `kubescape scan /caminho/manifestos --format json --output results.json` e em seguida roda `kubescape fix results.json` (com opções `--dry-run`, `--no-confirm` ou `--output-dir ./fixed` para preservar os originais; se o JSON veio de um scan de cluster vivo, os manifestos corrigidos são apenas impressos no stdout para eventual `kubectl apply -f -`). Para patching de imagens de container, o comando `kubescape patch --image <imagem> --tag <imagem-patched>` utiliza a ferramenta **Copacetic** e requer um daemon `buildkitd` ativo para atualizar apenas os pacotes de nível de sistema operacional vulneráveis em uma nova camada sobre a imagem existente, sem precisar do Dockerfile original.

## Exemplo
```bash
# Gerar relatório JSON de manifestos locais e visualizar as correções automáticas em modo dry-run
kubescape scan ./manifests --format json --output results.json
kubescape fix results.json --dry-run

# Aplicar patch de vulnerabilidades de SO em uma imagem usando buildkitd e Copacetic
sudo buildkitd &
sudo kubescape patch --image nginx:1.22 --tag nginx:1.22-patched -v
```

## Limites e trade-offs
O `kubescape fix` aplica valores seguros recomendados nos manifestos (como `allowPrivilegeEscalation: false`, `runAsNonRoot: true` ou limites de recursos), o que pode quebrar aplicações legadas que realmente tentam escrever na raiz do filesystem ou iniciar processos como UID 0 se não forem validadas em staging; já o `kubescape patch` (via Copacetic) corrige apenas vulnerabilidades de pacotes de sistema operacional (apt/apk/yum), não atualizando bibliotecas de aplicação compiladas (como módulos Go, JARs Java ou pacotes npm).

## Como verificar
Após executar `kubescape fix results.json --output-dir ./fixed`, rode `kubescape scan ./fixed` novamente para comprovar a redução de controles falhos; para imagens, escaneie a tag gerada (`kubescape scan image nginx:1.22-patched`) e confirme a eliminação dos CVEs de SO corrigíveis.

## Conexões
- [[kubescape-varredura-vulnerabilidades-imagens-grype-multi-arch]] — Veja também: Kubescape: varredura de vulnerabilidades (CVEs) em imagens de container com Grype e inferência multi-arquitetura.
- [[kubescape-validating-admission-policies-cel-kubernetes]] — Veja também: Kubescape: controle de admissão nativo com Validating Admission Policies (VAP) baseadas em CEL.
- [[kubescape-plataforma-seguranca-kubernetes-opa-regolibrary]] — Referência cruzada direta com kubescape-plataforma-seguranca-kubernetes-opa-regolibrary.

## Fontes
- [Kubescape GitHub — README.md (OPA/Regolibrary, Grype, Copacetic, VAP, Operator & MCP)](https://raw.githubusercontent.com/kubescape/kubescape/master/README.md) — README oficial do Kubescape documentando varredura de postura com OPA/Regolibrary, CVEs de imagens com Grype, auto-fix, patching com Copacetic, Validating Admission Policies (CEL) e MCP server; consultado em 2026-10-03.
- [Kubescape Official Documentation — In-Cluster Operator & Runtime Security](https://kubescape.io/docs/operator/) — Documentação oficial do operador in-cluster do Kubescape com monitoramento contínuo e detecção de ameaças em runtime via eBPF (Inspektor Gadget); consultado em 2026-10-03.
- [Kubescape — Official GitHub Repository](https://github.com/kubescape/kubescape) — Repositório oficial Apache-2.0 do Kubescape (CNCF Incubating); consultado em 2026-10-03.
