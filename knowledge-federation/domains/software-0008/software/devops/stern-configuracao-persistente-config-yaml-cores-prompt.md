---
id: software.devops.tranche10.000997
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

# Stern: arquivo de configuração persistente (~/.config/stern/config.yaml), customização de cores SGR e modo --prompt

## Em uma frase
O Stern permite salvar padrões globais para qualquer flag da CLI no arquivo **`~/.config/stern/config.yaml`** (ou via `--config` / `STERNCONFIG`), customizar a paleta de cores ANSI SGR de pods e containers (`--pod-colors`, `--container-colors`, `--diff-container`) e selecionar instâncias interativamente com **`--prompt` (`-p`)**.

## Por que importa
Digitar `--tail 20 --timestamps=short --max-log-requests 200` em absolutamente todos os comandos `stern` do dia a dia é repetitivo; além disso, usuários com daltonismo ou terminais de fundo claro precisam ajustar os códigos de cores SGR usados para destacar os nomes dos pods e containers.

## Como funciona
Conforme documenta a seção `config file` e a tabela de flags do README oficial: (1) **Config File (`~/.config/stern/config.yaml`)**: aceita pares `<flag-name>: <value>` em YAML (ex.: `tail: 10`, `max-log-requests: 999`, `timestamps: short`), podendo apontar para outro caminho com `--config` ou variável de ambiente **`STERNCONFIG`**; (2) **Customização de Cores**: `--diff-container` (`-d`) força cores diferentes para containers diferentes dentro do mesmo pod, enquanto `--pod-colors` e `--container-colors` aceitam listas separadas por vírgula de sequências SGR (Select Graphic Rendition, ex.: `"91,92,93,94,95,96"` para cores brilhantes); e (3) **Modo interativo (`--prompt` / `-p`)**: exibe um seletor interativo no terminal listando os valores encontrados da label padrão `app.kubernetes.io/instance` no namespace para você escolher qual aplicação acompanhar.

## Exemplo
```yaml
# Exemplo oficial de ~/.config/stern/config.yaml definindo valores padrão seguros e práticos para o dia a dia
tail: 10
max-log-requests: 999
timestamps: short
diff-container: true
```

## Limites e trade-offs
Conforme observa a descrição oficial da flag `--container-colors`, se você definir tanto `--pod-colors` quanto `--container-colors` (na linha de comando ou no `config.yaml`), **ambas as listas devem ter exatamente o mesmo comprimento (número de cores)**; caso `--container-colors` seja omitida, ela herda automaticamente os mesmos valores de `--pod-colors`.

## Como verificar
Crie o arquivo `~/.config/stern/config.yaml` com `tail: 10` e `timestamps: short` e execute `stern . -n kube-system` sem flags adicionais para confirmar a aplicação automática das preferências.

## Conexões
- [[stern-limites-concorrencia-max-log-requests-qps-burst-api]] — Veja também: Stern: controle de concorrência e proteção do API Server (--max-log-requests, --qps, --burst e --verbosity).
- [[stern-containers-efemeros-init-containers-ciclo-vida-pods]] — Veja também: Stern: acompanhamento automático de initContainers, ephemeralContainers (kubectl debug) e rollouts dinâmicos.
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.
- [[k9s-extensibilidade-plugins-hotkeys-aliases-views-skins]] — Referência cruzada direta com k9s-extensibilidade-plugins-hotkeys-aliases-views-skins.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
