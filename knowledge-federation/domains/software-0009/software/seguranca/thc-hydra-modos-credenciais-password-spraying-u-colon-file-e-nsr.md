---
id: software.seguranca.tranche16.001572
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

# Modos de Credenciais no THC-Hydra: **Password Spraying (`-u` Loop Around Users)**, Pares `login:pass` (**`-C`**), Verificações Extras (**`-e nsr`**) e Parada Imediata (**`-f` / `-F`**)

## Em uma frase
Por que rodar o Hydra no modo padrão com uma lista de 50 usuários (`-L usuarios.txt`) e uma lista de 100 senhas (`-P senhas.txt`) contra um ambiente Active Directory / PAM com **`pam_faillock` (`deny = 5`)** vai **bloquear imediatamente a conta do primeiro usuário da lista** logo nos primeiros 5 segundos?

## Por que importa
Porque, como documenta a manpage `hydra(1)` para a flag **`-u`**: por padrão (sem `-u`), o Hydra testa **todas as 100 senhas seguidas no Usuário 1** antes de passar para o Usuário 2!

## Como funciona
Já quando você adiciona a flag **`-u` (*Loop around users — Password Spraying*)**, o Hydra inverte a ordem do loop: ele testa a **Senha 1 em todos os 50 usuários (apenas 1 tentativa por conta!)**, depois a Senha 2, e pode ser combinado com **`-c TIME`** (espera global entre tentativas com `-t 1`) para validar políticas de senha sem provocar bloqueio de contas (*Account Lockout*)!

## Exemplo
```bash
# Executar um teste controlado de credenciais padrao e verificacoes -e nsr (senha nula, igual ao login e reversa) parando no primeiro acerto (-f)
hydra -L ./contas_servico.txt -e nsr -u -f -t 4 ssh://192.0.2.10:22
hydra -C ./credenciais_padrao_fabricante.txt -f -t 4 ftp://192.0.2.10
```

## Limites e trade-offs
Olhe outras **3 flags valiosíssimas** no exemplo acima documentadas na manpage `hydra(1)`: **(1) `-e nsr`** — sem precisar de nenhuma wordlist externa, testa automaticamente para cada usuário três falhas clássicas de configuração: **`n`** (*Null password* / senha em branco), **`s`** (*Same as login* / senha idêntica ao próprio nome de usuário, ex.: `admin:admin` ou `postgres:postgres`) e **`r`** (*Reverse login* / nome do usuário invertido)!

## Como verificar
**(2) `-C arquivo.txt`** — lê pares já casados no formato `usuario:senha` (um por linha, perfeito para testar listas de *Default Vendor Credentials* como `root:root`, `admin:12345`, `tomcat:s3cret`!); e **(3) `-f` (e `-F`)** — encerra o teste no host imediatamente assim que encontrar o primeiro par `login:senha` válido!

## Conexões
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Veja também: Arquitetura do **THC-Hydra (`vanhauser-thc/thc-hydra`)**: Auditoria Paralelizada de Autenticação de Rede em Mais de 50 Protocolos (`SSH`, `RDP`, `SMB`, `HTTP-Form`, `LDAP`, `PostgreSQL`, `MySQL`, `SNMP`).
- [[thc-hydra-auditoria-formularios-web-http-post-form-get-form-cookies]] — Veja também: Auditando Formulários de Login Web e APIs com **`http-post-form` / `https-post-form`** no THC-Hydra: Sintaxe `"caminho:corpo:condicao"`, `F=` vs. `S=` e Headers `H=`.
- [[thc-hydra-controle-concorrencia-tasks-t-timeouts-w-restore-sessao-r]] — Referência cruzada direta com thc-hydra-controle-concorrencia-tasks-t-timeouts-w-restore-sessao-r.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
