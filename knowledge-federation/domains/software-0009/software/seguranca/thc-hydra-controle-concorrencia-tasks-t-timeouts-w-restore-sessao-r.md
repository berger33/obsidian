---
id: software.seguranca.tranche16.001574
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README", "https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Controle de Concorrência (**`-t` vs. `-T`**), Pausa Entre Tentativas (**`-W` / `-c`**), Retomada de Sessão (**`-R` `hydra.restore`**) e Saída JSON (**`-b json -o`**) no THC-Hydra

## Em uma frase
Qual é a diferença entre as flags **`-t TASKS`** e **`-T TASKS`** quando você audita uma lista de múltiplos servidores (`-M servidores.txt`) no THC-Hydra, e como evitar que um serviço legado (como SSH, RDP ou banco de dados) caia ou rejeite conexões por excesso de threads simultâneas?

## Por que importa
Na manpage `hydra(1)`: **(1) `-t TASKS`** (padrão `16`) define o número de conexões paralelas **por host alvo individual**; já **(2) `-T TASKS`** (padrão `64`) define o limite global de conexões paralelas **somando todos os hosts escaneados em paralelo via `-M`**!

## Como funciona
Por exemplo, no OpenSSH (`sshd_config`), a diretiva padrão `MaxStartups 10:30:100` começa a descartar conexões não autenticadas a partir de **10 conexões simultâneas**! Portanto, se você deixar o padrão `-t 16` contra um servidor SSH, o próprio `sshd` derrubará conexões e gerará falsos negativos — contra SSH e RDP, reduza sempre para **`-t 4`**!

## Exemplo
```bash
# Auditar uma lista de servidores (-M) com limite seguro de 4 conexoes por host (-t 4) salvando os resultados em formato JSON (-b json -o)
hydra -L ./usuarios.txt -P ./senhas.txt -u -f \
  -t 4 -T 32 -w 15 \
  -M ./servidores_ssh.txt \
  -b json -o ./resultado_hydra.json \
  ssh
```

## Limites e trade-offs
Veja duas outras funcionalidades operacionais importantes da manpage `hydra(1)`: **(1) Saída Estruturada em JSON (`-b json -o resultado.json` ou `-b jsonv1`)** — facilita importar os resultados validados diretamente em pipelines de automação com `jq`; e **(2) Retomada de Sessão (`hydra -R`)** — se você interromper uma execução com `Ctrl+C` (ou se ela parar por timeout), o Hydra grava o estado exato no arquivo **`hydra.restore`**; basta rodar `hydra -R` para continuar exatamente do ponto onde parou (ou passar `-I` para ignorar um `hydra.restore` antigo)!

## Como verificar
Para testes furtivos e lentos que simulam tentativas espaçadas no tempo, use **`-t 1 -c 30`** (1 única conexão esperando 30 segundos entre cada tentativa de login).

## Conexões
- [[thc-hydra-auditoria-formularios-web-http-post-form-get-form-cookies]] — Veja também: Auditando Formulários de Login Web e APIs com **`http-post-form` / `https-post-form`** no THC-Hydra: Sintaxe `"caminho:corpo:condicao"`, `F=` vs. `S=` e Headers `H=`.
- [[thc-hydra-auditoria-bancos-dados-postgres-mysql-mssql-redis-mongodb]] — Veja também: Auditando Autenticação de Bancos de Dados (**PostgreSQL, MySQL/MariaDB, MS-SQL, Redis, MongoDB e Oracle**) com o THC-Hydra.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.
- [[thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr]] — Referência cruzada direta com thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
