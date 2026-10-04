---
id: software.devops.tranche10.001000
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/stern/stern/master/README.md", "https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md", "https://github.com/stern/stern"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Stern: instalação via Krew/Homebrew/asdf/WinGet, precedência de KUBECONFIG e autocompletar de shell (--completion)

## Em uma frase
O Stern pode ser instalado como plugin oficial do `kubectl` via **Krew** (`kubectl krew install stern`, invocável como `kubectl stern`), além de Homebrew, `asdf`, WinGet ou `go install`, oferecendo autocompletar dinâmico de nomes de pods/deployments para `bash`, `zsh` e `fish` via **`--completion`**.

## Por que importa
Em ambientes Kubernetes, o autocompletar de shell (`--completion`) do Stern não completa apenas nomes de flags estáticas — ele consulta o cluster ativo para autocompletar com `<TAB>` os nomes de `deployment/...`, `statefulset/...`, `service/...` e namespaces (`-n`), acelerando drasticamente a operação na linha de comando.

## Como funciona
Conforme documentam as seções `Installation` e `Usage` do README oficial: (1) **Instalação**: disponível via `brew install stern`, `kubectl krew install stern`, `asdf plugin add stern && asdf install stern latest`, `winget install stern.stern` ou `go install github.com/stern/stern@latest`; (2) **Precedência de `KUBECONFIG`**: o Stern utiliza a variável de ambiente **`$KUBECONFIG`** se estiver definida (suportando múltiplos arquivos separados por `:` no Linux/macOS), mas se tanto `$KUBECONFIG` quanto a flag **`--kubeconfig`** forem passados, a flag da CLI `--kubeconfig` tem precedência; e (3) **Shell Completion**: executar **`source <(stern --completion bash)`** (ou `zsh` / `fish`) registra o autocompletar interativo no shell atual.

## Exemplo
```bash
# Instalar o Stern via Krew (como plugin kubectl stern) e habilitar o autocompletar no shell atual
kubectl krew install stern
source <(stern --completion bash)
```

## Limites e trade-offs
Quando instalado via **Krew** (`kubectl krew install stern`), o binário é instalado em `~/.krew/bin/kubectl-stern`, permitindo invocá-lo como subcomando nativo **`kubectl stern deployment/meu-app`**; se você também quiser invocá-lo apenas como `stern` (ou dentro de plugins padrão do K9s que chamam `command: stern`), crie um link simbólico ou instale-o também no `$PATH` padrão.

## Como verificar
Execute `stern --completion bash | head -n 20` para verificar a geração do script de autocompletar e confirme a versão com `stern --version`.

## Conexões
- [[stern-pipeline-jq-only-log-lines-raw-color-control]] — Veja também: Stern: integração em pipelines Unix com jq (--only-log-lines / -o raw, --color) e funções de tempo (toUTC, toTimestamp).
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.
- [[stern-configuracao-persistente-config-yaml-cores-prompt]] — Referência cruzada direta com stern-configuracao-persistente-config-yaml-cores-prompt.
- [[k9s-extensibilidade-plugins-hotkeys-aliases-views-skins]] — Referência cruzada direta com k9s-extensibilidade-plugins-hotkeys-aliases-views-skins.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
