---
id: software.seguranca.tranche15.001460
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md", "https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Formatos Dinâmicos Customizados (**`--format=dynamic=...`**) e Análise Estatística de Senhas Quebradas no John the Ripper

## Em uma frase
E quando você está auditando um sistema legado ou aplicação web antiga que inventou seu próprio esquema de hash composto no código-fonte — por exemplo, `sha256(md5($pass) . $salt . " ConstanteSecreta")` ou `md5(sha1($salt . $pass))` — que não corresponde a um formato fixo padrão? Precisa escrever código C novo e recompilar o John?

## Por que importa
Não! O **John the Ripper Jumbo** possui o motor de **Dynamic Formats (`--format=dynamic=<expressão>`)** otimizado com instruções SIMD (`AVX2`/`AVX-512`)!

## Como funciona
Você escreve a fórmula matemática da aplicação diretamente na linha de comando ou no `john.conf` (ex.: **`--format='dynamic=sha256(md5($p).$s)'`**) e o John monta em tempo de execução o pipeline vetorizado SIMD para avaliar aquela combinação exata de primitivas (`md5`, `sha1`, `sha256`, `sha512`, concatenações de `$p` senha, `$s` salt, `$u` username e constantes `$c1`) sem compilar uma única linha de C!

## Exemplo
```bash
# Testar e fazer benchmark de um formato dinamico composto customizado (sha256(md5($p).$s)) diretamente na linha de comando do John Jumbo
john --test=2 --format='dynamic=sha256(md5($p).$s)'
john --list=subformats | head -n 15
```

## Limites e trade-offs
Ao concluir uma auditoria autorizada de senhas na sua organização, **nunca inclua as senhas em texto claro dos funcionários no relatório PDF executivo**: utilize a saída do `john --show` em um script local seguro para extrair apenas **métricas agregadas de governança** (ex.: `% de senhas quebradas em menos de 1 hora`, `% de reutilização da mesma senha entre contas diferentes`, `comprimento médio` e `padrões mais comuns como NomeDaEmpresa+Ano`) e force a troca imediata das contas afetadas!

## Como verificar
Apague com segurança (`shred -u`) todos os dumps de hashes (`ntds.dit`, `shadow_combinado.txt`, `john.pot`) da estação de auditoria assim que o ciclo de remediação for concluído.

## Conexões
- [[john-execucao-distribuida-fork-node-mpi-opencl-gpu-aceleracao]] — Veja também: Escalando o John the Ripper em Múltiplos Núcleos, GPUs e Clusters: **`--fork=N`**, **`--node=MIN-MAX/TOTAL`**, OpenMP e Formatos **`-opencl`**.
- [[john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes]] — Referência cruzada direta com john-arquitetura-john-the-ripper-jumbo-formatos-potfile-sessoes.
- [[john-unshadow-auditoria-senhas-unix-linux-etc-passwd-shadow-crypt]] — Referência cruzada direta com john-unshadow-auditoria-senhas-unix-linux-etc-passwd-shadow-crypt.

## Fontes
- [John the Ripper Jumbo Official GitHub Repository (`openwall/john`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/README.md) — repositório oficial do Openwall John the Ripper Jumbo cobrindo mais de 400 formatos de hash/arquivos cifrados, aceleração SIMD/OpenCL e utilitários `*2john`; consultado em 2026-10-03.
- [John the Ripper Official Cracking Modes Specification (`doc/MODES`)](https://raw.githubusercontent.com/openwall/john/bleeding-jumbo/doc/MODES) — especificação oficial dos modos de ataque do John the Ripper detalhando `Single Crack` (GECOS), `Wordlist` com regras de mangling, `Incremental` (cadeias de Markov) e `External`; consultado em 2026-10-03.
